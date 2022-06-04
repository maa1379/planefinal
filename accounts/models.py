from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel

from .managers import MyUserManager
from .uitils import get_file_path


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره تلفن",
    )

    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name="ادمین")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    # def __str__(self):
        # return self.phone_number

    @property
    def is_staff(self):
        return True

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    code = models.PositiveSmallIntegerField(verbose_name="کد ارسالی")
    created = models.DateTimeField(auto_now=True, verbose_name="تاریخ ارسال")

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"

    class Meta:
        verbose_name = "کد  ارسالی"
        verbose_name_plural = "کد های ارسالی"
