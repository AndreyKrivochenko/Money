from django.db import models

from catalogapp.models import Counterparties, CategoryUnit, Category


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

    def add_operation(self, price):
        self.summ += price

    def inc_operation(self, price):
        self.summ -= price

    def __str__(self):
        return self.title


class AccountOperation(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='счёт')
    counterparty = models.ForeignKey(Counterparties, on_delete=models.CASCADE, verbose_name='контрагент')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория операции')
    category_unit = models.ForeignKey(CategoryUnit, on_delete=models.CASCADE, verbose_name='название операции')
    price = models.DecimalField(verbose_name='стоимость операции', max_digits=8, decimal_places=2)
    comment = models.TextField(verbose_name='комментарий', blank=True)
    data = models.DateField(verbose_name='Дата операции')
    created_at = models.DateTimeField(verbose_name='Дата создания записи', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления записи', auto_now=True)

    def __str__(self):
        return f'{self.category.category_type.name}: {self.category_unit} - {self.price} руб.'
