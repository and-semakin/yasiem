from django.db import models
from django.core.urlresolvers import reverse


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='os/%Y-%m-%d', null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset:AssetListByCategory', args=[self.id])


class AssetUser(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Пользователь актива'
        verbose_name_plural = 'Пользователи активов'

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    ipv4 = models.CharField(max_length=15, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    os = models.ForeignKey(OperatingSystem, related_name='OperatingSystem', verbose_name="Операционная система")
    user = models.ForeignKey(AssetUser, related_name='User', verbose_name="Пользователь актива", null=True,
                             default=None)

    class Meta:
        ordering = ['name']
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('asset:AssetDetail', args=[self.slug, self.id])
