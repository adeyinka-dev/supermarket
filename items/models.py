from django.db import models
from djmoney.models.fields import MoneyField


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(decimal_places=2, max_digits=8, default_currency="NGN")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
