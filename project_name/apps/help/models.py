from django.db import models
from django.utils.translation import ugettext_lazy as _
from project_name.apps.core.utils.fields import BaseModel

class Help(BaseModel):
# Create your models here.
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    class Meta:
        verbose_name = _("Help")
        verbose_name_plural = _("Helps")
        unique_together = ['name']

    def __str__(self):
        return self.name