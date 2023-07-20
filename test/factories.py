import factory
from faker import Faker

from product.models import Discount, ProductCategory, ProductInventory  # Product,

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


# class ProductFactory(factory.django.DjangoModelFactory):
#     product_category = ProductCategoryFactory()
#     inventory = ProductInventoryFactory()
#     discount = DiscountFactory()

#     name = factory.Faker('name')
#     description = factory.Faker('text')
#     sku = fake.ean(length=13)
#     category_id = product_category.id
#     inventory_id = inventory.id
#     price = fake.pydecimal(left_digits=3, right_digits=2)
#     discount_id = discount.id

#     class Meta:
#         model = Product
