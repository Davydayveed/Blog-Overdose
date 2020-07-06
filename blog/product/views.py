from django.shortcuts import render

# Create your views here.

def product_detail(request):

    return render(request, "product-detail.html", {})
