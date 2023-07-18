from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    is_employee = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return "{}".format(self.email)


class UserAddress(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=60)
    postal = models.CharField(max_length=10)
    telephone1 = models.CharField(max_length=15)
    telephone2 = models.CharField(max_length=15)
    modified_at = models.DateTimeField(auto_now=True)


class UserPayment(models.Model):
    user_id = models.IntegerField()
    payment_type = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    account_number = models.IntegerField()
    expiry = models.DateField()
    modified_at = models.DateTimeField(auto_now=True)


class ShoppingSession(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    session_id = models.OneToOneField(
        ShoppingSession,
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        "product.Product", verbose_name=_("product id"), on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
