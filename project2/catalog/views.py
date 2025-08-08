from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from .models import Product, Order, OrderItem
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

def order(request):
    cart = Cart(request)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            address_2=address2,
            city=city,
            state=state,
            zip_code=zip_code
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity']
            )

        cart.clear()
        return redirect('index')
    return render(request, 'catalog/order.html', {'cart': cart})
