from django.views.generic import TemplateView
from common.constants import ACCOUNT_MENU


class AccountMainTemplateView(TemplateView):
    template_name = 'accountapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMainTemplateView, self).get_context_data()
        context['title'] = 'Счета'
        context['account_menu'] = ACCOUNT_MENU
        return context


class AccountServicesTemplateView(TemplateView):
    template_name = 'accountapp/account_services.html'

    def get_context_data(self, **kwargs):
        context = super(AccountServicesTemplateView, self).get_context_data()
        context['title'] = 'Услуги'
        context['account_menu'] = ACCOUNT_MENU
        return context


class AccountPropertyTemplateView(TemplateView):
    template_name = 'accountapp/account_property.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPropertyTemplateView, self).get_context_data()
        context['title'] = 'Имущество'
        context['account_menu'] = ACCOUNT_MENU
        return context
