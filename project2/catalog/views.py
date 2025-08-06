from django.shortcuts import render
from django.views import View

from .models import Product


def index(request):
    queryset = Product.objects.all()
    return render(request, 'catalog/index.html', {'queryset': queryset})