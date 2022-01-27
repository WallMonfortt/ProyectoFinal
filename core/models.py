from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def create_user(self,name, apellido, email, password, **extra_fields):
        if not email:
            raise ValueError('Por favor ingresa un email')
        name = name.strip()
        apellido = apellido.strip()
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Is staff necesita ser verdadero")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Is superuser necesita ser verdadero")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self) -> str:
        return self.email