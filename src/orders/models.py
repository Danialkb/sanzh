from django.db import models
from django.db.models import Sum

from dishes.models import Dish
from orders.choices import OrderStatus
from users.models import User
from zones.models import Table


class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=30,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="orders",
    )
    table = models.ForeignKey(
        Table,
        null=True,
        on_delete=models.SET_NULL,
        related_name="orders",
    )

    class Meta:
        db_table = "orders"


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=30, choices=OrderStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    dish = models.ForeignKey(
        Dish,
        null=True,
        on_delete=models.SET_NULL,
        related_name="order_items",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.total_amount = self.order.items.aggregate(
            total=Sum(models.F("dish__price") * models.F("quantity"))
        )["total"] or 0
        self.order.save(update_fields=["total_amount"])

    def delete(self, *args, **kwargs):
        order = self.order
        super().delete(*args, **kwargs)
        order.total_amount = order.items.aggregate(
            total=Sum(models.F("dish__price") * models.F("quantity"))
        )["total"] or 0
        order.save(update_fields=["total_amount"])

    class Meta:
        db_table = "order_items"
