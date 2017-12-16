# Create your views here.
from django.views.generic import TemplateView,DetailView
from . import models
from django.http import JsonResponse
from .forms import ProyectForm


class ProjectView(TemplateView):
    template_name = 'themes/pages/project/project.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()        
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(ProjectView,self).get_context_data(**kwargs)
        form = ProyectForm(self.request.GET or None)
        context["form"] = form
        return context

class ProjectResultsView(DetailView):
    model = models.Project
    template_name = 'themes/pages/project/project_result.html'

class ProjectListView(TemplateView):
    model = models.Project
    template_name = 'themes/pages/project/project_list.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = models.Project.objects.all() 
        return context
        
class ProjectDetailView(DetailView):
    """docstring for ProjectDetailView"""
    model = models.Project
    template_name = 'themes/pages/project/project_detail.html'

    '''def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['now'] = "hola soy goku"
        return context'''

def save_datos_generales(request): 
    # username = request.GET
    # models.Project.save()
    form = ProyectForm(request.GET or None)
    data = {'form_is_valid':form.is_valid()}
    if data['form_is_valid']:
        form.save()
    else:
        data['form_errors'] = form.errors.as_json()
    return JsonResponse(data)