from django.contrib.auth.models import User
from rest_framework import serializers

# Auth stuff
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password
# from django.db import models
# from rest_framework.permissions import IsAuthenticated

from .models import Cart, ShoppingSession, User, UserAddress, UserPayment


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "email", "password", "first_name", "last_name")
#         extra_kwargs = {
#             "password": {"write_only": True},
#         }

#         def create(self, validated_data):
#             user = User.objects.create_user(
#                 # validated_data['username'], email is username
#                 password=validated_data["password"],
#                 first_name=validated_data["first_name"],
#                 last_name=validated_data["last_name"],
#                 email=validated_data["email"],
#             )
#             return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    extra_kwargs = {"password": {"write_only": True}}


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
