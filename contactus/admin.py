from django.contrib import admin
from . import models
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'lname']
    list_editable = ['email']


admin.site.register(models.ContactUs)
