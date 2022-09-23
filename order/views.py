from django.shortcuts import render
from .forms import NewDeliveryMethodForm, NewOrderForm
from django.contrib import messages
from django.http import JsonResponse
from products.models import Product
# Create your views here.
def order_home(request):

    context = {
        
    }

    return render(request, 'order/order_home.html', context)


def new_delivery_method(request):
    form = NewDeliveryMethodForm()
    context = {
        'form': form
    }

    if request.method == "POST":
        form = NewDeliveryMethodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Delivery Method Saved')
    return render(request, 'order/new_delivery_method.html', context)

def new_order(request):
    form = NewOrderForm()
    context = {
        'form': form
    }

    if request.method == "POST":
        skus = request.POST.getlist('fsku')
        print(skus)
        qtys = request.POST.getlist('fqty')
        print(qtys)

        


    return render(request, 'order/new_order.html', context)


def load_order_data(request):
    data = []

    porducts_data = Product.objects.all()

    for obj in porducts_data:
        item = {
            'name': obj.name,
            'sku': obj.sku,
            'sell_price': obj.sell_price,
            'stock_qty': obj.stock_qty,
        }

        data.append(item)
    return JsonResponse({
        'data': data,
    })
