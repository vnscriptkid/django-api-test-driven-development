from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **args):
        """Create and save a new user"""
        if not email:
            raise ValueError('missing email')
        if not password:
            raise ValueError('missing password')
        user = self.model(
            email=self.normalize_email(email.lower()),
            **args
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
