from django.urls import path
from . import views

urlpatterns = [
    path('new_product/', views.new_product, name='new_product'),
    path('new_product_category/', views.new_product_category, name='new_product_category'),
    path('new_product_brand/', views.new_product_brand, name='new_product_brand'),
]
