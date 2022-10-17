from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your models here.

class products(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    noElements = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def delete_all_url(self):
        return reverse("products.delete", kwargs={"id": self.id})

    def create_element(request):
        return redirect(request, "products.create")

    def get_edit_url(self):
        return reverse("products.edit", kwargs={"pk": self.id})
