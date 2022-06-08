import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from django.views.generic import ListView
from .forms import UserDocumentForm, UserProfileForm
from .models import Profile, UserDocument

logger = logging.getLogger("__name__")


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

class Test(LoginRequiredMixin, View):
    def get(self, request):
        user_document = UserDocument.objects.filter(user=self.request.user)
        return render(request, 'profiles/upload.html', {'object_list': user_document})

    def post(self, request):
        user = request.user
        my_list = []
        images = request.FILES.getlist('image[]')
        for file in images:
            obj = Image_Doc.objects.create(file=file)
            my_list.append(obj.id)
        for key, value in dict(request.POST).items():
            for i in range(0, len(value)):
                # if len(user_docs) > i:
                #     user_doc = user_docs[i]
                # else:
                user_doc = UserDocument()
                if key == "madrak":
                    user_doc.title = value[i]
                elif key == "description":
                    user_doc.description = value[i]
                    user_doc.image = my_list[i]
                    user_doc.user = user
                    user_doc.save()
                # UserDocument.objects.ce(user_docs)
            # if len(user_docs) > i:
            #     user_docs[i] = user_docs
            # else:
            #     user_docs.append(user_doc)

        return redirect("accounts:dashboard")
