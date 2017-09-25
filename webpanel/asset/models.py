from django.db import models
from django.core.urlresolvers import reverse
from .notify_telegram import notify


# класс Операционная система
class OperatingSystem(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Название')
    image = models.ImageField(upload_to='os/%Y-%m-%d', null=True,
                              verbose_name='Логотип')

    class Meta:
        ordering = ['name']
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset:AssetListByOs', args=[self.id])


# класс Пользователь актива
class AssetUser(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True,
                            verbose_name='Ссылка')

    class Meta:
        ordering = ['name']
        verbose_name = 'Пользователь актива'
        verbose_name_plural = 'Пользователи активов'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset:AssetListByUser', args=[self.id])


# класс Актив
class Asset(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Название')
    ipv4 = models.CharField(max_length=15, db_index=True,
                            verbose_name='IP адрес')
    slug = models.SlugField(max_length=200, db_index=True, unique=True,
                            verbose_name='Ссылка')
    os = models.ForeignKey(OperatingSystem, related_name='asset',
                           verbose_name="Операционная система")
    user = models.ForeignKey(AssetUser, related_name='asset',
                             verbose_name="Пользователь актива",
                             null=True, default=None)

    class Meta:
        ordering = ['name']
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset:AssetDetail', args=[self.slug, self.id])


# класс Тип инцидента безопасности
class AlertType(models.Model):
    ALERT_LEVELS = (
        (0, 'низкий'),
        (1, 'средний'),
        (2, 'высокий')
    )
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Название')
    level = models.SmallIntegerField(choices=ALERT_LEVELS, default=0,
                                     verbose_name='Уровень важности')

    class Meta:
        verbose_name = 'Тип инцидента'
        verbose_name_plural = 'Типы инцидентов'

    def __str__(self):
        return self.name


# класс Инцидент безопасности
class Alert(models.Model):
    type = models.ForeignKey(AlertType, verbose_name='Тип инцидента',
                             db_index=True, related_name='alert')
    asset = models.ForeignKey(Asset, verbose_name='Актив', db_index=True,
                              related_name='alert')
    time = models.DateTimeField(db_index=True, auto_now=True,
                                verbose_name='Время возникновения')
    checked = models.BooleanField(default=False, db_index=True,
                                  verbose_name='Отработано')
    checked_message = models.CharField(max_length=512, blank=True,
                                       verbose_name='Пояснительное сообщение')
    # TODO: добавить связь с событиями из ElasticSearch.
    # Здесь как-то нужно хранить идентификаторы событий.

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'

    def save(self, *args, **kwargs):
        super(Alert, self).save(*args, **kwargs)
        notify(text="<b>{}</b> произошел инцидент безопасности <b>\"{}\"</b> "
               "на активе <b>\"{}\"</b> (IP: {}, пользователь: <b>{}</b>). "
               "Инциденту присвоен <b>{}</b> уровень критичности.\n"
               "Детали: http://127.0.0.1:8000{}".
               format(self.time.strftime("%d.%m.%Y %H:%M:%S"), self.type.name,
                      self.asset.name, self.asset.ipv4, self.asset.user.name,
                      self.type.get_level_display(), self.get_absolute_url()))

    def __str__(self):
        return "{} {} {}".format(self.time, self.type.name, self.asset.name)

    def get_absolute_url(self):
        return reverse('asset:AlertDetails', args=[self.id])


# класс Событие
class Event(models.Model):
    source = models.CharField(max_length=256, null=True)
    dt = models.CharField(max_length=256, null=True)
    user = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=256, null=True)
    data = models.CharField(max_length=512, null=True)
