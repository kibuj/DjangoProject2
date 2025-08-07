from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from .models import Product
from .cart import Cart

def index(request):
    queryset = Product.objects.all()

    #Пошук
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        queryset = queryset.filter(title__icontains=item_name)

    paginator = Paginator(queryset, 4)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    return render(request, 'catalog/index.html', {'queryset': queryset})

def detail(request, id):
    queryset = Product.objects.get(id=id)
    return render(request, 'catalog/detail.html', {'queryset': queryset})

def add_to_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product)
    return redirect('cart_detail')

def remove_from_cart(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'catalog/cart_detail.html', {'cart': cart})

