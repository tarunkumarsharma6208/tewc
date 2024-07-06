from django import forms
from .models import Product, Brands, ProductImage
from django.forms import modelformset_factory

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category', 'brand', 'name',  'rate', 'discount_percentage', 
            'description', 'seller', 'start_date', 'end_date', 'stock'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'seller': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



ProductImageFormSet = modelformset_factory(
    ProductImage,
    form=ProductImageForm,
    extra=4,  # Number of extra forms to display
    can_delete=True  # Allow deletion of images
)
