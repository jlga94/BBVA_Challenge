from django.contrib import admin

from .models import CRUDEvent, LoginEvent


@admin.register(CRUDEvent)
class CRUDEventAdmin(admin.ModelAdmin):
    list_display = ['get_event_type_display', 'content_type', 'object_id', 'object_repr', 'user', 'datetime']


@admin.register(LoginEvent)
class LoginEventAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'get_login_type_display', 'username', 'user']
