from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.utils.fields import BaseModel


class Country(BaseModel):
    code = models.CharField(
        _('code'), max_length=80, blank=True, null=True)
    country = models.CharField(
        _('country'), max_length=150, blank=True, null=True)
    status = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        unique_together = ['code']

    def __str__(self):
        return self.country


class State(BaseModel):
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_country")
    state = models.CharField(
        _('state'), max_length=200, blank=True, null=True)
    status = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")
        unique_together = ['country', 'state']

    def __str__(self):
        return self.state


class City(BaseModel):
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_country")
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_state")
    city = models.CharField(
        _('city'), max_length=80, blank=True, null=True)
    latitude = models.FloatField(
        _('latitude'), null=True, blank=True, default=None)
    longitude = models.FloatField(
        _('longitude'), null=True, blank=True, default=None)
    status = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.city
