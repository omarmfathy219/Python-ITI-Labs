from django.contrib import admin

# Register your models here.


from products.models import products
admin.site.register(products)
