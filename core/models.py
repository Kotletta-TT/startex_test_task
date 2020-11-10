from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractBaseUser):
    email = models.EmailField(_("e-mail"), unique=True)
    first_name = models.CharField(_("Имя"), max_length=25)
    last_name = models.CharField(_("Фамилия"), max_length=30)
    patronic_name = models.CharField(_("Отчетсво"), max_length=30)
    address_shipment = models.CharField(_("Адрес доставки"), max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def natural_key(self):
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
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(CustomUser, related_name="carts", on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return self.user