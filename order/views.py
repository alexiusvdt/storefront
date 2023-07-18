from rest_framework import viewsets

from .models import OrderDetails, OrderItems, PaymentDetails
from .serializers import (
    OrderDetailsSerializer,
    OrderItemsSerializer,
    PaymentDetailsSerializer,
)


class PaymentDetailsView(viewsets.ModelViewSet):
    serializer_class = PaymentDetailsSerializer
    queryset = PaymentDetails.objects.all()


class OrderDetailsView(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class OrderItemsView(viewsets.ModelViewSet):
    serializer_class = OrderItemsSerializer
    queryset = OrderItems.objects.all()
