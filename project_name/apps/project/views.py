# Create your views here.
from django.views.generic import TemplateView
from . import models
from django.http import JsonResponse

class ProjectView(TemplateView):
    template_name = 'themes/pages/project/project.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectListView(TemplateView):
    template_name = 'themes/pages/project/project_list.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = models.Project.objects.all() 
        return context

def save_datos_generales(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': 'te salio'
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)