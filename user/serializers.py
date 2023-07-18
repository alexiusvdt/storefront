from rest_framework import serializers

from .models import Cart, ShoppingSession, User, UserAddress, UserPayment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            "id",
            "user_id",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal",
            "country",
            "telephone1",
            "telephone2",
            "modified_at",
        ]
        read_only_fields = ["modified_at", "id"]


class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = [
            "id",
            "user_id",
            "payment_type",
            "provider",
            "account_number",
            "expiry",
        ]
        read_only_fields = [
            "id",
        ]


class ShoppingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = [
            "id",
            "user_id",
            "total",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["id", "created_at", "modified_at"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "session_id",
            "product_id",
            "quantity",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["id", "session_id", "created_at", "modified_at"]
