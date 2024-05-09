from django.contrib import admin
from .models import slider
# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    admin.site.register(slider)
# Register your models here.
