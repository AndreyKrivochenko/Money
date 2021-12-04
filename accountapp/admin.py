from django.contrib import admin

from accountapp.models import AccountType, Account, AccountOperation

admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(AccountOperation)
