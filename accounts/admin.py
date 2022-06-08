from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from profiles.models import Profile, UserDocument

from .forms import ChangeForm, CreationForm
from .models import OtpCode, User


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserDocumentInLine(admin.StackedInline):
    model = UserDocument
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine, UserDocumentInLine]
    form = CreationForm
    add_form = ChangeForm

    list_display = ("phone_number",)
    list_filter = ("is_admin",)
    readonly_fields = ("last_login",)

    fieldsets = (
        (
            "اطلاعات اصلی",
            {"fields": ("phone_number",)},
        ),
        (
            "دسترسی ها",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = ((None, {"fields": ("phone_number",)}),)
    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["is_superuser"].disabled = True
        return form


admin.site.register(User, UserAdmin)
admin.site.register(OtpCode)
