from django.contrib import admin

from accountapp.models import AccountType, Account

admin.site.register(AccountType)
admin.site.register(Account)
