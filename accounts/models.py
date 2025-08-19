from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not username:
            raise ValueError('Users must have a username')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phone_number=phone_number
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)

        return user

    def create_staffuser(self, username, phone_number, email, password=None):
        return self.create_user(
            username=username,
            phone_number=phone_number,
            email=email,
            password=password,
            is_active=True,
            is_staff=True
        )

    def create_superuser(self, username, phone_number, email, password=None):
        return self.create_user(
            username=username,
            phone_number=phone_number,
            email=email,
            password=password,
            is_active=True,
            is_staff=True,
            is_admin=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.email  # You can also return self.username if preferred

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
