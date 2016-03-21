from django.contrib import admin
from .models import MediaTest

# Register your models here.
@admin.register(MediaTest)
class MediaTestAdmin(admin.ModelAdmin):
    pass