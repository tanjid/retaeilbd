from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_home, name='purchase_home'),
    path('new_purchase/', views.new_purchase, name='new_purchase'),

]
