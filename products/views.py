from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
# Create your views here.
def new_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/new_product.html', context)