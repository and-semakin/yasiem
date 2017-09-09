from django.contrib import admin
from .models import OperatingSystem, Asset

# ������ ���������
class OsAdmin(admin.ModelAdmin):
    list_display = ['name']

# ������ ������
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'ipv4', 'os']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(OperatingSystem, OsAdmin)
admin.site.register(Asset, AssetAdmin)
