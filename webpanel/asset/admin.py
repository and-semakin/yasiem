from django.contrib import admin
from .models import OperatingSystem, Asset, AssetUser


# администрирование операционных систем
class OsAdmin(admin.ModelAdmin):
    list_display = ['name']


# администрирование активов
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'ipv4', 'os']
    prepopulated_fields = {'slug': ('name', )}


# администрирование пользователей активов
class AssetUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(OperatingSystem, OsAdmin)
admin.site.register(AssetUser, AssetUserAdmin)
admin.site.register(Asset, AssetAdmin)
