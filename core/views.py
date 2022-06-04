from django.shortcuts import render
from django.views import View

from .models import ContactUs, WorkWith, Rules, AboutUs
from django.views.generic import CreateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ContactUsForm, WorkWithForm


# Create your views here.
class ContactUsView(SuccessMessageMixin, CreateView):
    model = ContactUs
    success_url = reverse_lazy('passengers:home')
    success_message = 'پیام شما با موفقیت ثبت شد'
    form_class = ContactUsForm
    template_name = 'core/contact_us.html'


class WorkWithView(SuccessMessageMixin, CreateView):
    model = WorkWith
    success_url = reverse_lazy('passengers:home')
    success_message = 'پیام شما با موفقیت ثبت شد'
    form_class = WorkWithForm
    template_name = 'core/work.html'


class RulesView(TemplateView):
    template_name = 'core/rules1.html'



class AboutUsView(View):
    def get(self, request):
        about = AboutUs.objects.first()
        return render(request, 'core/about_us.html', {'obj': about})
