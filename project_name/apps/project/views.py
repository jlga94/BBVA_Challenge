from django.views.generic import TemplateView


# Create your views here.

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
        return context
