from django.views.generic import TemplateView


class TransactionView(TemplateView):
    template_name = 'themes/pages/transaction/transaction.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransactionAssociateView(TemplateView):
    template_name = 'themes/pages/transaction/transaction_associate.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
