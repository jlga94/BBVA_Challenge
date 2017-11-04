from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core import constants as core_constants
from .manager import TeamManager, PermissionManager
from .utils.fields import BaseModel2


class Team(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)

    objects = TeamManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class Role(BaseModel2):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,
                             blank=True, null=True)
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    class Meta:
        unique_together = ('team', 'name', 'codename',)
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return "{0}:{1}".format(str(self.team.name), str(self.codename))

    def natural_key(self):
        return (self.name,)


class Permission(BaseModel2):
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    objects = PermissionManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class SpacePlans(BaseModel2):
    plan_choice = core_constants.SELECT_DEFAULT \
                  + core_constants.TYPE_PLAN_OPTIONS
    plan_type = models.CharField(
        _('plan type'), choices=plan_choice,
        max_length=80, default=core_constants.CODE_PLAN_ONE)
    size = models.PositiveSmallIntegerField(default=0)
    price_soles = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_dollars = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_initial = models.DateField(blank=True, null=False)
    date_final = models.DateField(blank=True, null=True)
    coin_kas = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('plan_type', 'date_initial', 'date_final')
        verbose_name = _('space plan')
        verbose_name_plural = _('space plans')

    def get_size_text(self):
        return "{0} GB".format(str(self.size))

    def __str__(self):
        return "{0}({1}) - {2}GB".format(str(self.plan_type), str(self.get_plan_type_display()), str(self.size))


class PaymentPlans(BaseModel2):
    name = models.CharField(_('name'), max_length=100, unique=True)
    description = models.TextField(_('description'))
    total_row = models.PositiveSmallIntegerField(default=0)
    total_column = models.PositiveSmallIntegerField(default=0)
    price_soles = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_dollars = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_initial = models.DateField(blank=True, null=False)
    date_final = models.DateField(blank=True, null=True)
    coin_kas = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _('payment plan')
        verbose_name_plural = _('payment plans')

    def __str__(self):
        return "row:{0} - column:{1}".format(str(self.total_row), str(self.total_column))
