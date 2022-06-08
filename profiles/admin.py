from django.contrib import admin
from .models import Profile, UserDocument,Image_Doc

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserDocument)
admin.site.register(Image_Doc)
