from django.urls import reverse_lazy
from django.views.generic import TemplateView

MAIN_MENU = {
    'Главная': {'class': 'nav-link', 'href': reverse_lazy('mainapp:main_page'), 'app': 'mainapp'},
    'Учёт': {'class': 'nav-link', 'href': reverse_lazy('accountapp:main_page'), 'app': 'accountapp'},
    'Бюджет': {'class': 'nav-link disabled', 'href': '#', 'app': ''},
    'Календарь': {'class': 'nav-link disabled', 'href': '#', 'app': ''},
    'Цели': {'class': 'nav-link disabled', 'href': '#', 'app': ''},
    'Отчёты': {'class': 'nav-link disabled', 'href': '#', 'app': ''},
    'Справочники': {'class': 'nav-link', 'href': reverse_lazy('catalogapp:main_page'), 'app': 'catalogapp'},
}

ACCOUNT_MENU = {
    'main_page': ['accountapp:main_page', 'Счета'],
    'services': ['accountapp:services', 'Услуги'],
    'property': ['accountapp:property', 'Имущество'],
}

CATALOG_MENU = {
    'main_page': ['catalogapp:main_page', 'Категории'],
    'counterparties': ['catalogapp:counterparties', 'Контрагенты']
}


class TemplateViewWithMenu(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TemplateViewWithMenu, self).get_context_data()
        context.update({
            'account_menu': ACCOUNT_MENU,
            'main_menu': MAIN_MENU,
            'catalog_menu': CATALOG_MENU,
        })
        return context
