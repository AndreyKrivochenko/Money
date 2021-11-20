from django.db import models


class AccountType(models.Model):
    title = models.CharField(max_length=64, verbose_name='название типа счёта')

    def get_full_summ(self):
        full_summ = 0
        for akk in Account.objects.filter(account_type=self):
            full_summ += int(akk.summ)
        return full_summ

    def get_all_account(self):
        return Account.objects.filter(account_type=self)

    def __str__(self):
        return self.title


class Account(models.Model):
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, verbose_name='тип счёта')
    title = models.CharField(max_length=128, verbose_name='название счёта')
    summ = models.DecimalField(verbose_name='сумма счёта', max_digits=8, decimal_places=2)
