from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Project

class ProyectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name','description','periods','contractor','resident','supervisor','execution_time','start_date','end_date',)
        widgets = {
        	'description' : forms.Textarea(attrs={'rows':'3'}),
        	'start_date': forms.TextInput(attrs={'type':'date'}),
            'end_date': forms.TextInput(attrs={'type':'date'}),
        }
        labels = {
            'name': _('Nombre del Proyecto'),
			'description': _('Descripción'),
			'periods': _('Periodo de Control'),
			'contractor': _('Contratista'),
			'resident': _('Residente'),
			'supervisor': _('Supervisor'),
			'execution_time': _('Plazo de Ejecución'),
			'start_date': _('Inicio de Proyecto'),
			'end_date': _('Fin de Proyecto'),
        }
"""class ProyectForm(forms.ModelForm):
    name = forms.CharField(label='Nombre del Proyecto', max_length=100)
    description = forms.CharField(label='Descripción',widget=forms.Textarea(attrs={'rows':'3'}))
    periods = forms.IntegerField(label='Periodo de Control')
    contractor = forms.CharField(label='Contratista', max_length=100)
    resident = forms.CharField(label='Residente', max_length=100)
    supervisor = forms.CharField(label='Supervisor', max_length=100)
    execution_time = forms.CharField(label='Plazo de Ejecución', max_length=100)
    start_date = forms.DateField(label='Inicio de Proyecto',widget=forms.TextInput(attrs={'type':'date'}))
    end_date = forms.DateField(label='Fin de Proyecto',widget=forms.TextInput(attrs={'type':'date'}))"""