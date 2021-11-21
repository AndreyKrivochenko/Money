from common.constants import TemplateViewWithMenu


class CatalogMainTemplateView(TemplateViewWithMenu):
    template_name = 'catalogapp/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogMainTemplateView, self).get_context_data()
        context.update({
            'title': 'Категории',
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
