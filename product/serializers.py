from rest_framework import serializers

from .models import Discount, Product, ProductCategory, ProductInventory

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


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "modified_at",
            "closed_at",
        ]
        read_only_fields = ["created_at", "modified_at", "closed_at"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            "id",
            "name",
            "description",
            "discount_percent",
            "active",
            "created_at",
            "modified_at",
            "closed_at",
        ]
        read_only_fields = ["created_at", "modified_at", "closed_at"]
