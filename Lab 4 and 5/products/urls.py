from django.urls import path
from products.views import products_index, products_home, products_list, products_form, show, delete, CreateProductView, create_prod, UpdateProductView

urlpatterns = [
    path("all", products_index),
    path("home", products_home),
    path("list", products_list),
    path("form", products_form),
    path("delete/<id>", delete, name="products.delete"),
    path("<int:id>", show, name="products.show"),
    path("create", CreateProductView.as_view(), name="products.create"),
    path("edit/<int:pk>", UpdateProductView.as_view(), name="products.edit")


]
