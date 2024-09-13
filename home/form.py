from django import forms
from home.models import Product


class ImageForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=("id","image")
        
