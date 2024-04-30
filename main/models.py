<<<<<<< HEAD
import hashlib
import time
import uuid

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from main import error


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    recommendations = models.TextField(blank=True, null=True)

    def get_info(self):
        info = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email
        }

        return info


class Meet(models.Model):
    """Модель представляет собой описание встречи."""
    id = models.CharField(max_length=11, primary_key=True, unique=True)
    name = models.CharField(max_length=256, null=True)
    creator = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="group_creator", null=True
    )
    place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(to=User, related_name="users")

    @staticmethod
    def generate_unique_id():
        """Генерирует уникальный идентификатор для встречи."""
        for _ in range(1000):
            id_meet = hashlib.sha256(
                str(f"{time.time()}{uuid.uuid4().hex}".replace(
                    '.', uuid.uuid4().hex)).encode('utf-8')
            ).hexdigest()[:11]
            if not Meet.objects.filter(id=id_meet).exists():
                return id_meet

        raise error.DatabaseError(
            'Ошибка при создании идентификатора встречи! Возможно, превышен лимит интеграций для генерации идентификаторов.'
        )

    def save(self, *args, **kwargs):
        """Overrides the default save method to set a unique ID before saving."""

        if not self.id:
            try:
                self.id = self.generate_unique_id()
            except error.DatabaseError:
                raise error.DatabaseError()
            except Exception:
                raise error.CriticalError()

        super().save(*args, **kwargs)


class Place(models.Model):
    name = models.CharField(max_length=256)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )
    path_image = models.TextField(blank=True, null=True)


class History(models.Model):
    """История посещений встреч пользователем."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meet = models.ForeignKey(Meet, on_delete=models.CASCADE)
=======
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
>>>>>>> 98fd232f868e088baf30d1c41b8f43f1ab3cd5cc
