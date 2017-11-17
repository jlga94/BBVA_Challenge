# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from project_name.apps.core.utils.fields import BaseModel

class Project(BaseModel):
# Create your models here.
    name = models.CharField(max_length=100)
    description = models.TextField()
    periods = models.IntegerField()
    contractor = models.CharField(max_length=100)
    resident = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    execution_time = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Project")
        unique_together = ['name']

    def __str__(self):
        return self.name