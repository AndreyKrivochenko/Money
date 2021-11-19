from django.urls import path
import accountapp.views as accountapp

app_name = 'accountapp'

urlpatterns = [
    path('', accountapp.AccountMainTemplateView.as_view(), name='main_page'),
]
