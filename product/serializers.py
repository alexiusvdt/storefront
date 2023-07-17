from rest_framework import serializers

from .models import Product

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
        exclude = ["id"]
        read_only_fields = ["created_at"]
