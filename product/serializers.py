from rest_framework import serializers

from .models import Product, ProductInventory

# https://www.geeksforgeeks.org/modelserializer-in-serializers-django-rest-framework/#


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "sku",
            "category_id",
            "inventory_id",
            "price",
            "discount_id",
            "created_at",
            "modified_at",
            "deleted_at",
        ]
        read_only_fields = ["created_at"]


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "quantity",
            "created_at",
            "modified_at",
            "closed_at",
        ]
        read_only_fields = ["created_at", "modified_at", "closed_at"]
