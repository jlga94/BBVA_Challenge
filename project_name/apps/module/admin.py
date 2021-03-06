# Register your models here.
from django.contrib import admin

from .models import (
    Module, ModuleItem, RoleModule, RoleModuleItem
)


class ModuleItemAdminInline(admin.TabularInline):
    model = ModuleItem
    extra = 0


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'match', 'reference', 'order']
    inlines = [ModuleItemAdminInline]


class ModuleItemTeamAdminInline(admin.TabularInline):
    list_display = ['module_team', 'moduleitem']
    model = RoleModuleItem
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "moduleitem":
            if request._obj is not None:
                pass
                field.queryset = ModuleItem.objects.filter(module=request._obj.module)
            else:
                field.queryset = field.queryset.none()
        return field


@admin.register(RoleModule)
class ModuleTeamAdmin(admin.ModelAdmin):
    list_display = ['module', 'role', 'get_moduleitem_list', 'get_module_order']
    inlines = [ModuleItemTeamAdminInline]
    ordering = ('module__order',)

    def get_form(self, request, obj=None, **kwargs):
        request._obj = obj
        return super().get_form(request, obj, **kwargs)
