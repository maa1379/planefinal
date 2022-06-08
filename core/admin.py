from django.contrib import admin

# Register your models here.
from .models import AboutUs, ContactUs, Rules, Service, SiteSetting

admin.site.register(SiteSetting)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(Service)
admin.site.register(Rules)
