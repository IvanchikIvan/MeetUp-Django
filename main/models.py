from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Meet(models.Model):
    """Модель представляет собой описание встречи."""

    group_name = models.CharField(max_length=50)
    group_color = models.CharField(max_length=30, default="green")  # записать цвет словом, например "green"
    group_creator = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                      blank=True, null=True,
                                      related_name="group_creator")  # пользователь, который создал группу
    users = models.ManyToManyField(to=User, related_name="users")


class UserRecommend(models.Model):
    """Модель предоставляет рекомендации, адаптированные к конкретному пользователю."""

    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True)

    # тут будут рекомендации
