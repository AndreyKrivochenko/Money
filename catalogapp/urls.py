from django.urls import path
import catalogapp.views as catalogapp

app_name = 'catalogapp'

urlpatterns = [
    path('', catalogapp.CatalogMainTemplateView.as_view(), name='main_page'),
    path('counterparties/', catalogapp.CatalogCounterpartiesTemplateView.as_view(), name='counterparties'),
]
