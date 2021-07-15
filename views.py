from django.shortcuts import render
from .models import Products

def ProductPage(request):
    products = Products.objects.all()
    return render(request,'treeproducts.html',{'products':products})
