from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentDetails(models.Model):
    # this is to get around declaration order
    order_id = models.ForeignKey(
        "OrderDetails", verbose_name=_("order id"), on_delete=models.CASCADE
    )
    amount = models.DecimalField(_("payment amount"), max_digits=5, decimal_places=2)
    provider = models.CharField(_("provider"), max_length=50)
    status = models.CharField(_("status"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class OrderDetails(models.Model):
    user_id = models.OneToOneField(
        "user.User",
        verbose_name=_("user id"),
        on_delete=models.CASCADE,
    )
    total = models.DecimalField(
        _("total"),
        max_digits=5,
        decimal_places=2,
    )
    payment_id = models.OneToOneField(
        PaymentDetails,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItems(models.Model):
    order_id = models.ForeignKey(
        OrderDetails,
        verbose_name=_("order id"),
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        "product.Product",
        verbose_name=_("product id"),
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(_("quantity"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        get_latest_by = "modified_at"
