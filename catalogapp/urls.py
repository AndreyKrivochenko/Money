from django.urls import path
import catalogapp.views as catalogapp

app_name = 'catalogapp'

urlpatterns = [
    path('', catalogapp.CatalogMainTemplateView.as_view(), name='main_page'),
    path('create/', catalogapp.CatalogCreateCategoryView.as_view(), name='create_category'),
    path('create/unit/<int:pk>/', catalogapp.CatalogCreateUnitCategoryView.as_view(), name='create_unit_category'),
    path('counterparties/', catalogapp.CatalogCounterpartiesTemplateView.as_view(), name='counterparties'),
]
