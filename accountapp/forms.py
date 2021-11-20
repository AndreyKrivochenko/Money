from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms

from accountapp.models import Account, AccountType


class AccountCreateForm(BSModalModelForm):
    account_type = forms.ModelChoiceField(
        label='Тип счёта',
        queryset=AccountType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите тип счёта'
    )

    title = forms.CharField(
        label='Наименование',
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Наименование'}),
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
