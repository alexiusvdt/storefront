from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import OrderDetails, OrderItems, PaymentDetails
from .serializers import (
    OrderDetailsSerializer,
    OrderItemsSerializer,
    PaymentDetailsSerializer,
)


class PaymentDetailsViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):
    serializer_class = PaymentDetailsSerializer
    queryset = PaymentDetails.objects.all()


class OrderDetailsViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class OrderItemsViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
):

    serializer_class = OrderItemsSerializer
    queryset = OrderItems.objects.all()
