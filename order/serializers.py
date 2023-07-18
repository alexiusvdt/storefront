from rest_framework import serializers

from .models import OrderDetails, OrderItems, PaymentDetails

# https://www.geeksforgeeks.org/modelserializer-in-serializers-django-rest-framework/#
# laterbase : double check readable/allowable fields


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = [
            "id",
            "order_id",
            "amount",
            "provider",
            "status",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["created_at", "modified_at", "id"]


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = [
            "id",
            "user_id",
            "total",
            "payment_id",
            "created_at",
        ]
        read_only_fields = ["created_at", "modified_at", "id"]


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = [
            "id",
            "order_id",
            "product_id",
            "quantity",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["created_at", "modified_at", "id"]
