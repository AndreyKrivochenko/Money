from django import forms

from catalogapp.models import Category, CategoryType, CategoryUnit


class CatalogCategoryCreateForm(forms.ModelForm):
    category_type = forms.ModelChoiceField(
        label='Тип категории',
        queryset=CategoryType.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите тип категории'
    )

    name = forms.CharField(
        label='Наименование',
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'type': 'text', 'placeholder': 'Наименование'}),
    )

    class Meta:
        model = Category
        fields = ('category_type', 'name')


class CatalogUnitCategoryCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='',
        queryset=Category.objects.all(),
        widget=forms.HiddenInput(attrs={'class': 'form-control mb-2'}),
        empty_label='Выберите категорию'
    )

    name = forms.CharField(
        label='Наименование',
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'type': 'text', 'placeholder': 'Наименование'}),
    )

    class Meta:
        model = CategoryUnit
        fields = ['category', 'name']
