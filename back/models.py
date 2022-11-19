from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('A', 'Админ'),
        ('P', 'Пользователь'),
    )
    roles = models.CharField(choices=ROLES, max_length=2, blank=True,
                             default='S')

    class Meta:
        db_table = 'NewUsers'

    def __str__(self):
        return f'{self.username}'




