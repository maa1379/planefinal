from django.contrib import admin

from .models import Image_Doc, Profile, UserDocument

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserDocument)
admin.site.register(Image_Doc)
