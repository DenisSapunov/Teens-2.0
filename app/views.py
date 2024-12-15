from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()

    return render(request, "index.html", {"context": products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, "product_datail.html", {"context": product})

def category_product(request, category_id):
    products = Product.objects.filter(category=category_id)
    return render(request, "category.html", {"context": products})

