from django.urls import path
from . import views

urlpatterns = [
    path('new_product/', views.new_product, name='new_product'),
]
