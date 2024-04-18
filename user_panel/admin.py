from django.contrib import admin
from .models import AddAddress
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_filter = ['read_by_admin']
admin.site.register(AddAddress)