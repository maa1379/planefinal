import random

from braces.views import AnonymousRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, FormView, ListView, UpdateView,
                                  View)

from .forms import (LoginForm, PassChangeForm, RegisterForm, UserUpdateForm,
                    VerifyCodeForm)
from .models import OtpCode
from .uitils import send_otp

# from pyad import *

# pyad.set_defaults(ldap_server="IT-LHQ-DC1.LIFEALIKE.LAB", username='administrator@7bluesky.org', password="Siami@1399")
#
# ou = pyad.adcontainer.ADContainer.from_dn("ou=All_Users, dc=LIFEALIKE, dc=LAB")



# Create your views here.
user = get_user_model()


class UserLoginView(View):
    form_class = LoginForm
    register_form = RegisterForm
    template_name = "accounts/auth.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.path)
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(
            request, self.template_name, {"form": form, "register_form": RegisterForm}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, phone_number=cd["phone_number"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "با موفقیت وارد شدید", "info")
                return redirect("accounts:dashboard")
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است", "warning")
        return render(request, self.template_name, {"form": form})


# class UserLoginView(AnonymousRequiredMixin, FormView):
#     form_class = LoginForm
#     success_url = reverse_lazy("accounts:dashboard")
#     template_name = "accounts/auth.html"
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         cd = form.changed_data
#         user = authenticate(
#             self.request, user_name=cd["user_name"], password=cd["password"]
#         )
#         if user is not None:
#             login(self.request, user)
#             messages.success(self.request, "", "success")
#         else:
#             messages.error(self.request, "", "danger")
#         return super(UserLoginView, self).form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context_data = super(UserLoginView, self).get_context_data(**kwargs)
#         context_data["register_form"] = RegisterForm
#         return context_data
#
#     def form_invalid(self, form):
#         print(form.errors)
#         messages.error(self.request, form.errors, "danger")
#         return super(UserLoginView, self).form_invalid(form)


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "با موفقیت از  حساب حود خارح شدید", "success")
        return redirect("accounts:login")


class UserRegisterView(AnonymousRequiredMixin, View):
    form_class = RegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp(form.cleaned_data["phone_number"], random_code)
            OtpCode.objects.create(
                phone_number=form.cleaned_data["phone_number"], code=random_code
            )
            request.session["user_registration_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
                "password": form.cleaned_data["password"],
            }
            messages.success(request, "کد برای شما ارسال شد", "success")
            return redirect("accounts:verify")
        else:
            messages.error(request,'کاربر با این شماره تلقن قبلا ثبت نام کرده')
            return redirect('accounts:login')


class UserRegisterVerifyCodeView(AnonymousRequiredMixin, View):
    form_class = VerifyCodeForm
    template_name = "accounts/verify.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.META.get("HTTP_REFERER") == "":
    #         return super(UserRegisterVerifyCodeView, self).dispatch(
    #             request, *args, **kwargs
    #         )
    #     raise Http404

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        user_session = request.session["user_registration_info"]
        code_instance = OtpCode.objects.filter(
            phone_number=user_session["phone_number"]
        ).last()
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["code"] == code_instance.code:
                user_obj = user.objects.create_user(
                    phone_number=user_session["phone_number"],
                    password=user_session["password"],
                )
                login(request, user_obj)
                new_user = pyad.aduser.ADUser.create(user_obj.phone_number, ou, password=form.cleaned_data['password'])
                code_instance.delete()
                messages.success(request, "you registered.", "success")
                return redirect("accounts:dashboard")
            else:
                messages.error(request, "this code is wrong", "danger")
                return redirect("accounts:verify")
        return redirect("accounts:verify")


class UserDashboard(LoginRequiredMixin, View):
    def get(self, request):
        user_obj = get_object_or_404(user, id=request.user.id)
        
        return render(request, "accounts/dashboard.html", {"user": user_obj})


class UserUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    def test_func(self, user):
        return self.get_object() == self.request.user

    model = user
    success_url = reverse_lazy("accounts:dashboard")
    template_name = "accounts/update.html"
    form_class = UserUpdateForm


class UserPassChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:dashboard")
    success_message = "رمز عبور با موفقیت تغییر یاقت"
    form_class = PassChangeForm

    def form_invalid(self, form):
        print(form.errors)
        return super(UserPassChangeView, self).form_invalid(form)



