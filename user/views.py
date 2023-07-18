from rest_framework import viewsets

from .models import Cart, ShoppingSession, User, UserAddress, UserPayment
from .serializers import (
    CartSerializer,
    ShoppingSessionSerializer,
    UserAddressSerializer,
    UserPaymentSerializer,
    UserSerializer,
)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAddressView(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()


class UserPaymentView(viewsets.ModelViewSet):
    serializer_class = UserPaymentSerializer
    queryset = UserPayment.objects.all()


class ShoppingSessionView(viewsets.ModelViewSet):
    serializer_class = ShoppingSessionSerializer
    queryset = ShoppingSession.objects.all()


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
