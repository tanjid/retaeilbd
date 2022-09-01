from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductCategoryForm, ProductBrandForm
# Create your views here.
def new_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'New Product is saved')
            


    return render(request, 'products/new_product.html', context)

def new_product_category(request):
    form = ProductCategoryForm()
    context = {
        'form': form
    }

    if request.method == "POST":
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Product Categorry Saved')
    return render(request, 'products/new_product_category.html', context)

def new_product_brand(request):
    form = ProductBrandForm()
    context = {
        'form': form
    }

    if request.method == "POST":
        form = ProductBrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Product Brand Saved')
    return render(request, 'products/new_product_brand.html', context)