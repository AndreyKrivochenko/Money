from django.urls import path
import catalogapp.views as catalogapp

app_name = 'catalogapp'

urlpatterns = [
    path('', catalogapp.CatalogMainTemplateView.as_view(), name='main_page'),
    path('create/', catalogapp.CatalogCreateCategoryView.as_view(), name='create_category'),
    path('create/unit/<int:pk>/', catalogapp.CatalogCreateUnitCategoryView.as_view(), name='create_unit_category'),
    path('create/counterparties/', catalogapp.CounterpartiesCreateView.as_view(), name='create_counterparties'),
    path('delete/<int:pk>/', catalogapp.CatalogCategoryDeleteView.as_view(), name='delete_category'),
    path('delete/unit/<int:pk>/', catalogapp.CatalogUnitCategoryDeleteView.as_view(), name='delete_unit_category'),
    path('counterparties/', catalogapp.CatalogCounterpartiesTemplateView.as_view(), name='counterparties'),
]
