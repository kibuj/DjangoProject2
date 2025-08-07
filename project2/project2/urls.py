from django.contrib import admin
from django.urls import path

from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
]
