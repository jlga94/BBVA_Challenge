from django.contrib import admin

from . import models


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SpacePlans)
class SpacePlanAdmin(admin.ModelAdmin):
    list_display = ["plan_type", "get_size_text", "coin_kas", "price_soles", "price_dollars"]


@admin.register(models.PaymentPlans)
class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ["total_row", "total_column", "coin_kas", "price_soles", "price_dollars"]

