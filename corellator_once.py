import os
import sys
import django
from django.utils.timezone import now
from datetime import datetime
from multiprocessing import Process
from time import sleep
import json
from elasticsearch import Elasticsearch
from art_time_generator.common_once import *


sys.path.append(os.path.join(os.path.dirname(__file__), "webpanel"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webpanel.settings")
django.setup()

from asset.models import (Asset, AssetUser, Alert,
                          AlertType, OperatingSystem)


def check_failed_login():
    es = Elasticsearch()
    while True:
        reply = es.search(index='2017-09-17', body={"query": {"match_phrase": {"act": "LOGIN FAILED"}}})
        # print(reply)
        if len(reply) >= 3:  # TODO: fix this condition
            print("LOGIN FAILED EXCEPTION")
        else:
            print("NO EXC, LISTENING . . .")
        sleep(10)


def corellate():
    p1 = Process(target=check_failed_login)
    p1.start()


def create_alert():
    type = AlertType.objects.all()[0]  # выбираем первый попавшийся тип инцидента
    asset = Asset.objects.all()[0]  # выбираем первый попавшийся актив
    alert = Alert.objects.create(type=type, asset=asset)  # создаем инцидент из этого всего.
    print(alert)


if __name__ == '__main__':
    corellate()
    # create_alert()
