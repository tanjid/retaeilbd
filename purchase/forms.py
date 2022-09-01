from django.forms import ModelForm
from django import forms
from .models import Purchase

class NewPurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(PurchaseForm, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})
