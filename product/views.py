from django.http import HttpResponse
from rest_framework import viewsets

from .models import Product, ProductInventory
from .serializers import ProductInventorySerializer, ProductSerializer

# from django.shortcuts import render
# request -> responses
# This is a request handler, not a viewer


def say_hello(request):
    return HttpResponse("hello world")


# The viewsets base class provides the implementation for CRUD operations by default.
# This code specifies the serializer_class and the queryset.
class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductInventoryView(viewsets.ModelViewSet):
    serializer_class = ProductInventorySerializer
    queryset = ProductInventory.objects.all()
