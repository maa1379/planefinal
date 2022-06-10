# Import the logging module
import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Import HttpResponse to send data to the browser
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, View

from .forms import UserDocumentForm, UserProfileForm
from .models import Profile, UserDocument

# Define the logging configurations
logging.config.dictConfig({
    # Define the logging version
    'version': 1,
    # Enable the existing loggers
    'disable_existing_loggers': False,

    # Define the formatters
    'formatters': {
        'console': {
            'format': '%(message)s'
        },
        'file': {
            'format': '%(message)s'
        },

        # Define the handlers
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'file',
                'filename': 'djangoapp.log'
            }
        },

        # Define the loggers
        'loggers': {
            'django': {
                'level': 'DEBUG',
                'handlers': ['file', 'console'],

            }
        }
    }

})

# Create the loggers object
logger = logging.getLogger('__name__')


# Create your views here.
class EditUserView(LoginRequiredMixin, View):
    form_class = UserProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile)
        return render(request, "profiles/edite.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "profile edited successfully", "success")
        return redirect("accounts:dashboard")


# class Test(View):
#     form_class = UserDocumentForm
#     template_name = "profiles/upload.html"
#
#     def get(self, request):
#         logger.error("Testing Django log...")
#         return render(request, self.template_name, {"form": self.form_class})
#
#     def post(self, request):
#         logger.error("Testing Django log...")
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user_doc = form.save(commit=False)
#             user_doc.user = self.request.user
#             user_doc.save()
#             messages.success(request, "", "success")
#         return redirect("accounts:dashboard")
from .models import Image_Doc


def handle_uploaded_file(f):
    destination = open('/tmp/upload/%s' % f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


from django.contrib.auth import get_user_model

user_obj = get_user_model()


class Test(LoginRequiredMixin, View):
    def get(self, request):
        user_document = UserDocument.objects.filter(user=self.request.user)
        logger.error("Testing Django log...by elyas")
        return render(request, 'profiles/upload.html', {'object_list': user_document})

    def post(self, request):
        user = user_obj.objects.first()
        my_list = []
        for image in request.FILES.getlist('images'):
            Image_Doc.objects.create(file=image)
        user_docs = []
        for key, value in dict(request.POST).items():
            for i in range(0, len(value)):
                if len(user_docs) > i:
                    user_doc = user_docs[i]
                else:
                    user_doc = UserDocument()
                    user_doc.user = user
                if key == "madrak":
                    user_doc.title = value[i]
                if key == "description":
                    user_doc.description = value[i]
                    # user_doc.image = my_list[i]
                    # user.save()
                if len(user_docs) > i:
                    user_docs[i] = user_doc
                else:
                    user_docs.append(user_doc)

        UserDocument.objects.bulk_create(user_docs)

        # if len(user_docs) > i:
        #     user_docs[i] = user_docs
        # else:
        #     user_docs.append(user_doc)

        return redirect("accounts:dashboard")
