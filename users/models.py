from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _



class PermissionMixin:
    pass


class User(AbstractBaseUser, PermissionMixin):
    username = models.CharField(_('username'), max_length=32, unique=True
                                help_text=_(
                                    'Required, 30 characters'
                                ),
                                validators.RegexValidator(r'^[a-zA-Z][a-zA-Z0-9_\.]+$'),








class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    nick_name =
    avatar =
    birthday =
    gender =
    province =

