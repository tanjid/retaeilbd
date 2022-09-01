from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('retailbd.urls')),
    path('products/', include('products.urls')),
    path('purchase/', include('purchase.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
]