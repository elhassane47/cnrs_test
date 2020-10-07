from django import forms
from core.models import Tablet, Brand


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'founder', 'country',)


class TabletForm(forms.ModelForm):

    release_year = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Tablet
        fields = ('name', 'brand', 'storage_size', 'release_year',)


