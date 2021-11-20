from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView

from accountapp.forms import AccountCreateForm
from accountapp.models import AccountType, Account
from common.constants import ACCOUNT_MENU


class AccountMainTemplateView(TemplateView):
    template_name = 'accountapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMainTemplateView, self).get_context_data()
        context['title'] = 'Счета'
        context['account_menu'] = ACCOUNT_MENU
        context['account_type'] = AccountType.objects.all()
        return context


class AccountCreateView(BSModalCreateView):
    template_name = 'accountapp/create_account_modal.html'
    form_class = AccountCreateForm
    success_url = reverse_lazy('accountapp:main_page')


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('accountapp:main_page')

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
