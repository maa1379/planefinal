from django.shortcuts import render
from .forms import UserProfileForm, UserDocumentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic import TemplateView
from .models import Profile, UserDocument
import logging
from django.contrib import messages
from django.shortcuts import redirect

logger = logging.getLogger('__name__')


# Create your views here.
class EditUserView(LoginRequiredMixin, View):
    form_class = UserProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile)
        return render(request, 'profiles/edite.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile edited successfully', 'success')
        return redirect('accounts:dashboard')


class Test(View):
    form_class = UserDocumentForm
    template_name = 'profiles/upload.html'

    def get(self, request):
        logger.error("Testing Django log...")
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        logger.error("Testing Django log...")
        form = self.form_class(request.POST)
        if form.is_valid():
            user_doc = form.save(commit=False)
            user_doc.user = self.request.user
            user_doc.save()
            messages.success(request, '', 'success')
        return redirect('account:dashboard')
