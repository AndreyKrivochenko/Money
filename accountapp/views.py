from django.views.generic import TemplateView


class AccountMainTemplateView(TemplateView):
    template_name = 'accountapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMainTemplateView, self).get_context_data()
        context['title'] = 'Счета'
        return context
