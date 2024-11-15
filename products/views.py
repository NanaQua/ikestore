from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def upload_product(request):
    if request.method == 'POST':
        product = Product(
            name=request.POST['productName'],
            description=request.POST['productDescription'],
            price=request.POST['productPrice'],
            image=request.FILES['productImage']
        )
        product.save()
        return JsonResponse({'message': 'Product uploaded successfully!'}, status=201)

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    results = [{'name': product.name, 'description': product.description, 'price': product.price} for product in products]
    return JsonResponse(results, safe=False)

def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})

def adminPage(request):
    return render(request, "adminpage.html")