from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.managers import UserManager


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = models.CharField(_('username'), max_length=150, blank=True)
    email = models.EmailField('Адрес электронной почты', unique=True)
    first_name = models.CharField('Иия', max_length=32, blank=True)
    last_name = models.CharField('Фимилия', max_length=32, blank=True)
    middle_name = models.CharField('Отчество', max_length=32, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
