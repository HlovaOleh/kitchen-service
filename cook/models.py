from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"
        ordering = ['-username']
