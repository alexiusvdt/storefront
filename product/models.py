from django.db import models

# blank=true, field is not required
# null sets null/notnull
# OneToOne is 1-1 relationship
# ManyToOne => class Car(models.Model) gets placed in the MANY slot
# manufacturer = models.ForeignKey(etc)
# a Car model has a Manufacturer – Manufacturer makes multiple cars but each Car only has one Manufacturer


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return int(self.quantity)


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
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


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
        null=True,
        blank=True,
    )
    # add timestamp on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # update when calling Model.save() and not QuerySet.update
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        get_latest_by = "created_at"

    def __str__(self):
        return self.name
