from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

user = settings.AUTH_USER_MODEL


# Create your models here.
class Profile(TimeStampedModel):
    user = models.OneToOneField(
        user,
        on_delete=models.CASCADE,
        related_name="profile",
        blank=True,
        null=True,
        verbose_name="کاربر",
    )
    first_name = models.CharField(
        max_length=125, verbose_name="نام ", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=125, verbose_name="نام خانوادگی", blank=True, null=True
    )
    email = models.EmailField(verbose_name="ایمیل", blank=True, null=True)
    birthday = models.DateField(blank=True, null=True, verbose_name="تاریخ تولئ")

    def __str__(self):
        return f"{self.user} profile"

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل"


# from storages.backends.sftpstorage import SFTPStorage
#
# SFS = SFTPStorage()


def get_image_path(instance, filename):
    user = smart_str(instance.user.profile.first_name)
    directory = '/' + user
    if not os.path.exists(directory):
        os.makedirs(directory)
    full_path = str(directory) + "/%s" % (filename)
    return full_path


class Image_Doc(models.Model):
    file = models.ImageField(upload_to=get_image_path)


class UserDocument(TimeStampedModel):
    TITLE = (
        ("شناسنامه", "شناسنامه"),
        ("کارت ملی", "کارت ملی"),
        ("پاسپورت", "پاسپورت"),
        ("سایر", "سایر"),
    )
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="docs", blank=True, verbose_name=""
    )
    title = models.CharField(
        max_length=125, choices=TITLE, blank=True, verbose_name="عنوان"
    )
    image = models.OneToOneField(Image_Doc, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="توضیحات")

    def __str__(self):
        return f"{self.user} docs"

    class Meta:
        verbose_name = "مدرک"
        verbose_name_plural = "مدارک"
