from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import ContactUsForm, WorkWithForm
from .models import AboutUs, ContactUs, Rules, WorkWith


# Create your views here.
class ContactUsView(SuccessMessageMixin, CreateView):
    model = ContactUs
    success_url = reverse_lazy("passengers:home")
    success_message = "پیام شما با موفقیت ثبت شد"
    form_class = ContactUsForm
    template_name = "core/contact_us.html"


class WorkWithView(SuccessMessageMixin, CreateView):
    model = WorkWith
    success_url = reverse_lazy("passengers:home")
    success_message = "پیام شما با موفقیت ثبت شد"
    form_class = WorkWithForm
    template_name = "core/work.html"


class RulesView(TemplateView):
    template_name = "core/rules1.html"


from django.shortcuts import get_object_or_404, redirect, render


class AboutUsView(View):
    def get(self, request):
        about = AboutUs.objects.first()
        return render(request, "core/about_us.html", {"obj": about})


# from django.shortcuts import render_to_response
from django.template import RequestContext


# HTTP Error 400
def bad_request(request):
    return render(request, '404.html')


def page_not_found(request):
    return render(request, '404.html')


def server_error(request):
    return render(request, '404.html')
