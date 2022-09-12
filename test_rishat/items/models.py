from django.contrib.auth.models import User
from django.db import models

RUB = "rub"
USD = "usd"
EUR = "eur"

CURRENCYS = (
    (RUB, RUB),
    (USD, USD),
    (EUR, EUR),
)


class Item(models.Model):
    """Модель товара."""

    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание", max_length=1000)
    price = models.IntegerField("Цена")
    currency = models.CharField(
        'Валюта', choices=CURRENCYS, max_length=3, default=RUB
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Order(models.Model):
    """Модель корзины покупок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Товар",
    )

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    def __str__(self):
        return f'{self.user} {self.product}'
