from django.db import models


class AccountType(models.Model):
    title = models.CharField(max_length=64, verbose_name='название типа счёта')

    def get_full_summ(self):
        full_summ = 0
        for summ in Account.objects.filter(pk=self.pk):
            full_summ += summ
        return full_summ


class Account(models.Model):
    type_name = models.ForeignKey(AccountType, on_delete=models.CASCADE, verbose_name='тип счёта')
    title = models.CharField(max_length=128, verbose_name='название счёта')
    summ = models.DecimalField(verbose_name='сумма счёта', max_digits=8, decimal_places=2)
