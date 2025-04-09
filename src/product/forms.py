from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'status', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", "placeholder": "Title"}),
            'category': forms.Select(attrs={'class': 'tg-select form-control'}),
            'description': forms.Textarea(attrs={'id': "summernote"})
        }