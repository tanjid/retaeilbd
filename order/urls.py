from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('new_delivery_method/', views.new_delivery_method, name='new_delivery_method'),
    path('new_order/', views.new_order, name='new_order'),
    path('load_order_data/', views.load_order_data, name='load_order_data'),

]