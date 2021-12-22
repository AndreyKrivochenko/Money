from django import forms

from accountapp.models import Account, AccountType, AccountOperation
from catalogapp.models import Counterparties, Category, CategoryUnit


class AccountCreateForm(forms.ModelForm):
    account_type = forms.ModelChoiceField(
        label='Тип счёта',
        queryset=AccountType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите тип счёта'
    )

    title = forms.CharField(
        label='Наименование',
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'type': 'text', 'placeholder': 'Наименование'}),
        required=False
    )

    summ = forms.DecimalField(
        label='Сумма остатка',
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Сумма'}),
    )

    class Meta:
        model = Account
        fields = ('account_type', 'title', 'summ')


class OperationCreateForm(forms.ModelForm):

    account = forms.ModelChoiceField(
        label='Счёт',
        queryset=Account.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите счёт',
    )

    counterparty = forms.ModelChoiceField(
        label='Контрагент',
        queryset=Counterparties.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите контрагента',
    )

    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите категорию',
    )

    category_unit = forms.ModelChoiceField(
        label='Приход/расход',
        queryset=CategoryUnit.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите расход/доход',
    )

    price = forms.DecimalField(
        label='Сумма',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-2'}),
    )

    data = forms.DateField(
        input_formats=['%d-%m-%Y'],
        label='Дата',
        widget=forms.DateInput(attrs={'class': 'form-control mb-2', 'data-toggle': 'datepicker'}),
    )

    comment = forms.CharField(
        label='Коментарий',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}),
        empty_value='Напишите коментарий',
        required=False,
    )

    class Meta:
        model = AccountOperation
        fields = ['account', 'counterparty', 'category', 'category_unit', 'price', 'comment', 'data']
