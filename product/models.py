from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField()


class ProductInventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField()


class Discount(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    inventory_id = models.OneToOneField(
        ProductInventory,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    discount_id = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
    )
    # add timestamp on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # update when calling Model.save() and not QuerySet.update
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    class Meta:
        ordering = ["name"]
        get_latest_by = "created_at"
