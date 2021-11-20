from django.urls import path
import accountapp.views as accountapp

app_name = 'accountapp'

urlpatterns = [
    path('', accountapp.AccountMainTemplateView.as_view(), name='main_page'),
    path('services/', accountapp.AccountServicesTemplateView.as_view(), name='services'),
    path('property/', accountapp.AccountPropertyTemplateView.as_view(), name='property'),
    path('create/', accountapp.AccountCreateView.as_view(), name='create_account'),
    path('delete/<int:pk>/', accountapp.AccountDeleteView.as_view(), name='delete_account'),
]
