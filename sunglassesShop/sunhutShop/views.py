from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products_men(request):
    products = Product.objects.filter(category="Men")
    return render(request, 'men.html', {'products':products})