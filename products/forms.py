from django.forms import ModelForm
from django import forms
from .models import Product, ProductCategory, ProductBrand

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(ProductForm, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(ProductCategory, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})

class ProductBrandForm(ModelForm):
    class Meta:
        model = ProductBrand
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(ProductBrand, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})