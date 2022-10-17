from django import forms
from products.models import products


class ProuctForm(forms.ModelForm):
    class Meta:
        model = products
        fields = '__all__'
