from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import product,offerproduct

# Create your views here.

def host(request):
    obj=product.objects.all()
    return render(request,"index.html",{'product':obj})
def offer(request):
    obj1=offerproduct.objects.all()
    return render(request,'index.html',{'offerproduct':obj1})

