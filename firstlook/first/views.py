from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

def home(request):
    context = {
        'name': 'Karthick',
        'age': 25
    }
    
    return render(request,'home.html',context)
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)