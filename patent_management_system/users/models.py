from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class CustomUser(AbstractUser):
    """ ethereum_address = models.CharField(max_length=42, blank=True)
    private_key = models.CharField(max_length=64, blank=True) """


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )