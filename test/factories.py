import factory
from faker import Faker

from product.models import Discount, ProductCategory, ProductInventory  # Product

# from django.contrib.contenttypes.fields import GenericForeignKey


fake = Faker()


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("text")
    description = factory.Faker("text")

    class Meta:
        model = ProductCategory


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    quantity = factory.Faker("pyint", min_value=0, max_value=1000)

    class Meta:
        model = ProductInventory


class DiscountFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")
    # should pass validation in model
    discount_percent = fake.pydecimal(left_digits=3, right_digits=2)
    active = fake.pybool()

    class Meta:
        model = Discount


# having trouble assigning FK to Product class. Either object not saving correctly or returning error "must be of type DiscountID"
# class ProductFactory(factory.django.DjangoModelFactory):
#     name = factory.Faker('name')
#     description = factory.Faker('text')
#     sku = fake.ean(length=13)
#     # category_id = GenericForeignKey()
#     # inventory_id = GenericForeignKey()
#     price = fake.pydecimal(left_digits=3, right_digits=2)
#     # discount_id = DiscountFactory()

#     class Meta:
#         model = Product
