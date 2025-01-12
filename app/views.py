from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import Product, Category


def index(request, products=None):
    if not  products:
        products = Product.objects.all()
        return render(request, "index.html", {"context": products})
    return render(request, "index.html", {"context": products})



def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, "product_datail.html", {"context": product})

def category_product(request, category_id):
    products = Product.objects.filter(category=category_id)
    return render(request, "category.html", {"context": products})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, "categories_list.html",
                  {"context": categories})

def search(request):
    products = Product.objects.filter(name__icontains=request.GET['search'])
    return index(request,products)



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("main:homepage")
	form = NewUserForm()
	return render (request=request, template_name="registration/registration.html", context={"register_form":form})