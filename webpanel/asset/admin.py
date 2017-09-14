from django.contrib import admin
from .models import OperatingSystem, Asset, AssetUser, AlertType, Alert


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


# администрирование типов тревог
class AlertTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']


# администрирование тревог
class AlertAdmin(admin.ModelAdmin):
    list_display = ['type', 'asset', 'time', 'checked', 'checked_message']


admin.site.register(OperatingSystem, OsAdmin)
admin.site.register(AssetUser, AssetUserAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(AlertType, AlertTypeAdmin)
admin.site.register(Alert, AlertAdmin)
