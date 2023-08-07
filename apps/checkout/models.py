from django.db import models
from apps.accounts.models import User


class BasePurchaseInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} ({self.quantity}) - {self.price}"


class CartItem(BasePurchaseInformation):
    pass


class PurchaseHistory(BasePurchaseInformation):
    purchase_date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Email')
    first_name = models.CharField(max_length=30,
                                  verbose_name='Име')
    last_name = models.CharField(max_length=30,
                                 verbose_name='Фамилия')
    telephone_number = models.CharField(max_length=15,
                                        verbose_name='Телефонен номер')

    address = models.CharField(max_length=200,
                               verbose_name='Адрес')

    cart = models.OneToOneField(CartItem, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.email

    def name(self):
        return f'{self.first_name} {self.last_name}'
