from django.shortcuts import render
from .models import Products
#this is view file for trees file
def ProductPage(request):
    products = Products.objects.all()
    return render(request,'treeproducts.html',{'products':products})
