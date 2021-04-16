from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
# from .mixins import CustomPermissionsMixin
# from apps.api.models import Project
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     # "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     if self.is_admin:
    #         return True
    #
    #     return super().has_perm(self, perm, obj)
    #
    # def has_module_perms(self, app_label):
    #     # "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return self.is_admin


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    project = models.ManyToManyField('api.Project', blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_token(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
