from django.db import models
from django.core.urlresolvers import reverse


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
        return reverse('asset:AssetListByCategory', args=[self.id])


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


# класс Тип тревоги
class AlertType(models.Model):
    ALERT_LEVELS = (
        (0, 'низкий'),
        (1, 'средний'),
        (2, 'высокий')
    )
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Название')
    level = models.SmallIntegerField(choices=ALERT_LEVELS, default=0,
                                     verbose_name='Уровень тревоги')

    class Meta:
        verbose_name = 'Тип тревоги'
        verbose_name_plural = 'Типы тревог'

    def __str__(self):
        return self.name


# класс Тревога
class Alert(models.Model):
    type = models.ForeignKey(AlertType, verbose_name='Тип тревоги',
                             db_index=True, related_name='alert')
    asset = models.ForeignKey(Asset, verbose_name='Актив', db_index=True,
                              related_name='alert')
    time = models.DateTimeField(db_index=True,
                                verbose_name='Время возникновения')
    checked = models.BooleanField(default=False, db_index=True,
                                  verbose_name='Отработано')
    checked_message = models.CharField(max_length=512, blank=True,
                                       verbose_name='Пояснительное сообщение')
    # TODO: добавить связь с событиями из ElasticSearch.
    # Здесь как-то нужно хранить идентификаторы событий.

    class Meta:
        verbose_name = 'Тревога'
        verbose_name_plural = 'Тревоги'

    def __str__(self):
        return "{} {} {}".format(self.time, self.type.name, self.asset.name)
