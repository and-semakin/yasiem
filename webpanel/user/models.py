from django.db import models
from django.contrib.auth.models import User


# Модель профиля пользователя
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(verbose_name='Телефон',
                             max_length=15, blank=True)
    position = models.CharField(verbose_name='Должность',
                                max_length=64, blank=True)
    tg_notify_alerts = models.BooleanField(default=False,
                                           verbose_name='Уведомлять об '
                                           'инцидентах через Telegram')
    tg_notify_events = models.BooleanField(default=False,
                                           verbose_name='Уведомлять о событиях'
                                           ' через Telegram')
    tg_user_id = models.CharField(max_length=64, blank=True,
                                  verbose_name='ID в Telegram (брать здесь:'
                                  ' https://t.me/userinfobot)')


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
