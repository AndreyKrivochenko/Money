from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView

from accountapp.forms import AccountCreateForm, OperationCreateForm
from accountapp.models import AccountType, Account, AccountOperation
from catalogapp.models import Category
from common.constants import TemplateViewWithMenu


class AccountMainTemplateView(TemplateViewWithMenu):
    template_name = 'accountapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(AccountMainTemplateView, self).get_context_data()
        context['title'] = 'Счета'
        context['account_type'] = AccountType.objects.all()
        return context


class AccountCreateView(CreateView):
    template_name = 'accountapp/create_account_modal_form.html'
    model = Account
    form_class = AccountCreateForm
    success_url = reverse_lazy('accountapp:main_page')


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('accountapp:main_page')


class OperationCreateView(CreateView):
    template_name = 'accountapp/create_operation_modal_form.html'
    form_class = OperationCreateForm
    model = AccountOperation
    success_url = reverse_lazy('accountapp:main_page')

    def post(self, request, *args, **kwargs):
        category = Category.objects.get(pk=request.POST['category'])
        account = Account.objects.get(pk=request.POST['account'])
        if category.category_type.name == 'Расход':
            account.inc_operation(int(request.POST['price']))
        else:
            account.add_operation(int(request.POST['price']))
        account.save()
        return super(OperationCreateView, self).post(request, *args, **kwargs)


class AccountServicesTemplateView(TemplateViewWithMenu):
    template_name = 'accountapp/account_services.html'

    def get_context_data(self, **kwargs):
        context = super(AccountServicesTemplateView, self).get_context_data()
        context['title'] = 'Услуги'
        return context


class AccountPropertyTemplateView(TemplateViewWithMenu):
    template_name = 'accountapp/account_property.html'

    def get_context_data(self, **kwargs):
        context = super(AccountPropertyTemplateView, self).get_context_data()
        context['title'] = 'Имущество'
        return context
