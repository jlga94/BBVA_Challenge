
# Create your views here.
from django.views.generic import TemplateView

from . import models

# Create your views here.

class HelpView(TemplateView):
    template_name = 'themes/pages/help/help.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        print("hola salio esto")
        print(context)

        return context


class HelpListView(TemplateView):
    template_name = 'themes/pages/help/help_list.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["help"] = models.Help.objects.all()
        
        return context
