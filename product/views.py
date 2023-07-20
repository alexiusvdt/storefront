# from rest_framework import viewsets
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Discount, Product, ProductCategory, ProductInventory
from .serializers import (
    DiscountSerializer,
    ProductCategorySerializer,
    ProductInventorySerializer,
    ProductSerializer,
)


# The viewsets base class provides the implementation for CRUD operations by default.
# This code specifies the serializer_class and the queryset.
class ProductViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductInventoryView(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    serializer_class = ProductInventorySerializer
    queryset = ProductInventory.objects.all()


class ProductCategoryView(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class DiscountView(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
