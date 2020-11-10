from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Класс-менеджер для создания и сохранения пользователей с e-mail вместо username
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Функция для создания и сохранения пользователя с email вместо username
        """
        if not email:
            raise ValueError(_("Email необходим"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Функция для создания и сохранения суперпользователей, работает через create_user
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)
