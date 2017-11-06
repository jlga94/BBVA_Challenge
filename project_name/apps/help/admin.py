from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Help)
class HelpAdmin(admin.ModelAdmin):
    pass
