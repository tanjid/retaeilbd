from django.shortcuts import render
from .forms import NewDeliveryMethodForm, NewOrderForm
from django.contrib import messages

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
