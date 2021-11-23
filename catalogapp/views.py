from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from catalogapp.forms import CatalogCategoryCreateForm, CatalogUnitCategoryCreateForm
from catalogapp.models import Category, CategoryType, CategoryUnit
from common.constants import TemplateViewWithMenu


class CatalogMainTemplateView(TemplateViewWithMenu):
    template_name = 'catalogapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogMainTemplateView, self).get_context_data()
        context.update({
            'title': 'Категории',
            'category_type_list': CategoryType.objects.all(),
        })
        return context


class CatalogCreateCategoryView(CreateView):
    form_class = CatalogCategoryCreateForm
    model = Category
    template_name = 'catalogapp/create_category_modal_form.html'
    success_url = reverse_lazy('catalogapp:main_page')


class CatalogCategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalogapp:main_page')


class CatalogCreateUnitCategoryView(CreateView):
    model = CategoryUnit
    form_class = CatalogUnitCategoryCreateForm
    template_name = 'catalogapp/create_unit_category_modal_form.html'
    success_url = reverse_lazy('catalogapp:main_page')

    def get_initial(self):
        initial = {
            'category': Category.objects.get(pk=self.kwargs['pk'])
        }
        return initial


class CatalogUnitCategoryDeleteView(DeleteView):
    model = CategoryUnit
    success_url = reverse_lazy('catalogapp:main_page')


class CatalogCounterpartiesTemplateView(TemplateViewWithMenu):
    template_name = 'catalogapp/catalog_counterparties.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogCounterpartiesTemplateView, self).get_context_data()
        context.update({
            'title': 'Контрагенты',
        })
        return context
