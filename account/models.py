from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    sts =(
        ("director", "director"),
        ("manager", "manager"),
        ("cashier", "cashier"),
        ("worker", "worker"),
    )
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    staff = models.CharField(choices=sts, max_length=255, default='worker')
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
