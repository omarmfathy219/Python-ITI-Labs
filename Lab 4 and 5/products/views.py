from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView

from products.models import products
from products.forms import ProuctForm
# Create your views here.


def products_index(request):
    return HttpResponse("this my products index")


def products_list(request):
    allProducts = [
        {'id': 1, 'name': 'iphone 12', 'image': 'iphone12.png'},
        {'id': 2, 'name': 'iphone 12 pro max', 'image': 'iphone12pm.png'},
        {'id': 3, 'name': 'iphone 13 pro max', 'image': 'iphone13pm.png'},
        {'id': 4, 'name': 'iphone 13', 'image': 'iphone13.png'}
    ]
    return render(request, "products/productsall.html", context={'products': allProducts})


def products_home(request):
    return render(request, "products/home.html")


def products_form(request):
    allPro = products.objects.all()
    return render(request, "products/form.html", context={'products': allPro})


def show(request, id):
    product = products.objects.get(pk=id)
    return render(request, "products/show.html", context={'products': product})


def delete(request, id):
    product = products.objects.get(pk=id)
    product.delete()
    return redirect("/products/form")


class UpdateProductView(UpdateView):
    model = products
    form_class = ProuctForm
    template_name = 'products/edit.html'
    success_url = "/products/form"


class CreateProductView(CreateView):
    model = products
    form_class = ProuctForm
    template_name = 'products/create.html'
    success_url = "/products/form"

#


def create_prod(request):
    if request.POST:
        product = products()
        product.name = request.POST["name"]
        product.image = request.POST["image"]
        product.noElements = request.POST["noElements"]
        product.save()
        return redirect('/products/form')
    myform = ProuctForm()
    return render(request, "products/create.html", context={"form": myform})
