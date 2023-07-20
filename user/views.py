from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Cart, ShoppingSession, User, UserAddress, UserPayment
from .serializers import (
    CartSerializer,
    ShoppingSessionSerializer,
    UserAddressSerializer,
    UserPaymentSerializer,
    UserSerializer,
)

# The viewsets base class provides the implementation for CRUD operations by default.
# This code specifies the serializer_class and the queryset.


class UserViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAddressViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()


class UserPaymentViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = UserPaymentSerializer
    queryset = UserPayment.objects.all()


class ShoppingSessionViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = ShoppingSessionSerializer
    queryset = ShoppingSession.objects.all()


class CartViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = CartSerializer
    queryset = Cart.objects.all()
