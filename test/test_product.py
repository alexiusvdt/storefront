# from django.test import TestCase
# # import unittest
# from requests import get

# from rest_framework.test import APIRequestFactory, RequestsClient
# from rest_framework import status

# class ProductTests(APIRequestFactory):

#   def test_put_product(self):
#     factory = APIRequestFactory()
#     request = factory.put(
#             '/products/',
#             {'id': 1,
#               "name" : "sweet t shirt",
#               "sku" : "l;aisjefo;ij",
#               "category_id" : "325",
#               "inventory_id" : "522",
#               "price" : 53.22,
#               "discount_id" : "15",
#               },
#               format='json',
#     )
#   self.assertEqual(response.status_code == 200)

# # Create your tests here.
# # class TestProductApi(unittest.TestCase):

# #   def test_getAll(products: str) -> dict:
# #       """queries the product endpoint and returns all"""
# #       r = get('localhost:8000/products/')
# #       assert
# #       return r

# # if __name__ == '__main__':
# #    unittest.main()
