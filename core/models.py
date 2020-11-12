from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    # CUSTOMER = 1
    # MANAGER = 2
    #
    # ROLE_CHOICES = (
    #     (CUSTOMER, 'Customer'),
    #     (MANAGER, 'Manager'),
    # )
    email = models.EmailField(_("e-mail"), unique=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    first_name = models.CharField(_("Имя"), max_length=25)
    last_name = models.CharField(_("Фамилия"), max_length=30)
    patronic_name = models.CharField(_("Отчетсво"), max_length=30)
    address_shipment = models.CharField(_("Адрес доставки"), max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Product(models.Model):
    sku = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=70)
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.sku


class Cart(models.Model):
    user = models.ForeignKey('core.CustomUser', related_name="cart", on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    # count_items = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return self.user

    # def save(self, *args, **kwargs):
    #     """Здесь будем считать сумму корзины"""
    #     pass
