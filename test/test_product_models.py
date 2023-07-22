import datetime
import decimal

from django.test import TestCase

from .factories import (  # ProductFactory,
    DiscountFactory,
    ProductCategoryFactory,
    ProductInventoryFactory,
)


class TestProductCategoryTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        category = ProductCategoryFactory()
        self.assertEqual(str(category), category.name)


class TestProductInventoryFactoryTestCase(TestCase):
    def test_int(self):
        """testing creation of a product inventory qty"""
        product = ProductInventoryFactory()
        self.assertIsInstance(product.quantity, int)


class TestDiscountFactoryTestCase(TestCase):
    def test_vals(self):
        """testing creation of a full discount instance"""
        discount = DiscountFactory()
        self.assertEqual(str(discount), discount.name)
        self.assertIsInstance(discount.description, str)
        self.assertIsInstance(discount.active, bool)
        self.assertIsInstance(discount.discount_percent, decimal.Decimal)
        self.assertIsInstance(discount.created_at, datetime.date)


# class TestProductFactoryTestCase(TestCase):
#     def test_vals(self):
#         """testing a product instance creation"""
#         product = ProductFactory()
#         self.assertEqual(str(product), product.name)
#         self.assertIsInstance(product.description, str)
#         self.assertIsInstance(product.sku, str)
#         # self.assertIsInstance(product.category_id, int)
#         # self.assertIsInstance(product.inventory_id, int)
#         self.assertIsInstance(product.price, decimal)
#         # self.assertIsInstance(product.discount_id, int)
