from random import randint

from django.contrib.auth.models import BaseUserManager
from django.db import models

from .utils.funct_dates import str_datetime as datetime


class TeamManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class PermissionManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, codename, app_label, model):
        return self.get(codename=codename, )


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, is_admin=False,
                     **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            username = "{0} {1}".format(str("User"), str(randint(0, 999999)))
        is_active = extra_fields.pop("is_active", True)
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username,
                          is_active=is_active, is_admin=is_admin,
                          last_login=datetime(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, **extra_fields)
