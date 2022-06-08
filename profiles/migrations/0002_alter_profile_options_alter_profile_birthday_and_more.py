# Generated by Django 4.0.5 on 2022-06-04 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name": "پروفایل", "verbose_name_plural": "پروفایل"},
        ),
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateField(blank=True, null=True, verbose_name="تاریخ تولئ"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
        migrations.AlterField(
            model_name="userdocument",
            name="description",
            field=models.TextField(blank=True, verbose_name="توضیحات"),
        ),
        migrations.AlterField(
            model_name="userdocument",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="", verbose_name="تصویر مدرک"
            ),
        ),
        migrations.AlterField(
            model_name="userdocument",
            name="title",
            field=models.CharField(
                blank=True,
                choices=[
                    ("شناسنامه", "شناسنامه"),
                    ("کارت ملی", "کارت ملی"),
                    ("پاسپورت", "پاسپورت"),
                    ("سایر", "سایر"),
                ],
                max_length=125,
                verbose_name="عنوان",
            ),
        ),
        migrations.AlterField(
            model_name="userdocument",
            name="user",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="docs",
                to=settings.AUTH_USER_MODEL,
                verbose_name="",
            ),
        ),
    ]
