# from django.test import TestCase

# from product.serializers import ProductInventorySerializer
# from .factories import ProductInventoryFactory


# class TestProductInventorySerializer(TestCase):
#     def test_model_fields(self):
#         """Serializer data matches the object for each field."""
#         serializer = ProductInventorySerializer()
#         product = ProductInventoryFactory()
#         for field_name in [
#             "id",
#             "quantity",
#             "created_at",
#             "modified_at",
#         ]:
#             self.assertEqual(
#                 serializer.data[field_name],
#                 getattr(product, field_name)
#             )
