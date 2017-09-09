from django.db import models
from django.contrib.auth.models import User

# Модель профиля пользователя
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    phone =  models.CharField(verbose_name='Телефон', max_length=15, blank=True)
    position =  models.CharField(verbose_name='Должность', max_length=64, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
