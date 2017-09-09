from django.contrib import admin
from .models import OperatingSystem, Asset

# Модель категории
class OsAdmin(admin.ModelAdmin):
    list_display = ['name']

# Модель товара
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'ipv4', 'os']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(OperatingSystem, OsAdmin)
admin.site.register(Asset, AssetAdmin)
