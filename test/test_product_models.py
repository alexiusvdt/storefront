from django.test import TestCase

from .factories import ProductCategoryFactory


class TestProductCategoryTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        category = ProductCategoryFactory()
        self.assertEqual(str(category), category.name)
