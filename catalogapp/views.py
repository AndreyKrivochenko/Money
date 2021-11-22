from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


class CatalogCounterpartiesTemplateView(TemplateViewWithMenu):
    template_name = 'catalogapp/catalog_counterparties.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogCounterpartiesTemplateView, self).get_context_data()
        context.update({
            'title': 'Контрагенты',
        })
        return context


class CatalogCreateCategoryView(CreateView):
    form_class = CatalogCategoryCreateForm
    model = Category
    template_name = 'catalogapp/create_category_modal_form.html'
    success_url = reverse_lazy('catalogapp:main_page')


class CatalogCreateUnitCategoryView(CreateView):
    model = CategoryUnit
    form_class = CatalogUnitCategoryCreateForm
    template_name = 'catalogapp/create_unit_category_modal_form.html'
    success_url = reverse_lazy('catalogapp:main_page')

    # def get_context_data(self, **kwargs):
    #     context = super(CatalogCreateUnitCategoryView, self).get_context_data(**kwargs)
    #     context['initial_category'] = Category.objects.get(pk=self.kwargs['pk'])
    #     return context
