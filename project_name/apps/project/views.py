# Create your views here.
from django.views.generic import TemplateView,DetailView
from . import models
from django.http import JsonResponse
from .forms import ProyectForm
import requests 
#import requests

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

class VistaPagosListView(TemplateView):
    template_name = 'themes/pages/project/pagos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()        
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PagosListView(TemplateView):
    model = models.Project
    template_name = 'themes/pages/project/project_list.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = models.Project.objects.all() 

        url = 'http://10.17.182.204:7000/pagos/' 
        params = {'cd_id_empresa': 1}

        r = requests.get(url, params=params)
        pagos = r.json()
        context["pagos"] = pagos
        return context

class DetallePagosListView(TemplateView):
    template_name = 'themes/pages/project/detalle_Pago.html'

    {
        "T009_Paypal":{
        "num_tarjeta":"1" ,
        "cod_csv":"1",
        "tit_apellidos":"Gonzalez Prada",
        "tit_nombres":"Victor",
        "tit_correo":"victor.gonz@gmail.com",
        }
    }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()        
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProjectDetailView(DetailView):
    """docstring for ProjectDetailView"""
    model = models.Project
    template_name = 'themes/pages/project/project_detail.html'
    #queryset = models.Project.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        #object = super(ProjectDetailView, self).get_object()
        form = ProyectForm(self.request.GET or None)
        context["form"] = form

        return context



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