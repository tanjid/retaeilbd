from django.forms import ModelForm
from django import forms
from .models import DeliveryMethod
from products.models import Product


class NewDeliveryMethodForm(ModelForm):
    class Meta:
        model = DeliveryMethod
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(NewDeliveryMethodForm, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})



class NewOrderForm(forms.Form):
    name = forms.CharField()
    number = forms.CharField()
    delivery_method = forms.ModelChoiceField(queryset=DeliveryMethod.objects.all())
    order_note = forms.CharField(widget=forms.Textarea())
    # sku = forms.ModelChoiceField(queryset=Product.objects.all())
    # qty = forms.IntegerField()
    price = forms.IntegerField()
    item_total = forms.IntegerField()
    sub_total = forms.IntegerField()
    advance = forms.IntegerField()
    discount = forms.IntegerField()
    delivery_charge = forms.IntegerField()
    grand_total = forms.IntegerField()