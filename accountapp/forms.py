from django import forms

from accountapp.models import Account, AccountType, AccountOperation


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


class AddOperationsForm(forms.ModelForm):

    class Meta:
        model = AccountOperation
        fields = ['account', 'counterparty', 'category', 'category_unit', 'price', 'comment', 'data']
