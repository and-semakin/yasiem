import os
import sys
import django
from django.utils.timezone import now
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "webpanel"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webpanel.settings")
django.setup()

from asset.models import (Asset, AssetUser, Alert,
                                   AlertType, OperatingSystem)

def create_alert():
    type = AlertType.objects.all()[0] # выбираем первый попавшийся тип инцидента
    asset = Asset.objects.all()[0] # выбираем первый попавшийся актив
    alert = Alert.objects.create(type=type, asset=asset) # создаем инцидент из этого всего.
    print(alert)

if __name__ == '__main__':
    create_alert()
