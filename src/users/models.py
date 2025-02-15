from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users import choices


class UserManager(BaseUserManager):
    @staticmethod
    def _validate_user(email: str):
        if not email:
            raise ValueError("Users must have an email address")

    def create_user(self, first_name: str, last_name: str, password: str, email: str, phone_number: str):
        self._validate_user(email=email)

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_active=True,
            user_type=choices.UserTypeChoices.Customer,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str = None):
        self._validate_user(email=email)

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()

        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    user_type = models.CharField(
        max_length=10,
        choices=choices.UserTypeChoices.choices,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_password_temporary = models.BooleanField(default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email}"


