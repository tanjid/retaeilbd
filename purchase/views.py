from django.shortcuts import render
from .forms import NewPurchaseForm
from products.models import Product
from django.contrib import messages
# Create your views here.


def purchase_home(request):

    context = {
        
    }

    return render(request, 'purchase/purchase_home.html', context)

def new_purchase(request):
    form = NewPurchaseForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = NewPurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            my_purchase = form.save(commit=False)
            my_purchase_sku = str(my_purchase.sku)
            my_purchase_qty = my_purchase.qty
            my_product = Product.objects.get(sku=my_purchase_sku)
            my_product.stock_qty += my_purchase_qty
            my_product.save()
            my_purchase.save()

            messages.success(request, f'New Purchase saved')
            


    return render(request, 'purchase/new_purchase.html', context)