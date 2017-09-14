from django.shortcuts import render, get_object_or_404
from .models import Asset, OperatingSystem, Alert, AlertType
from django.contrib.auth.decorators import login_required


# Страница с активами
@login_required
def AssetList(request, operation_system=None):
    oses = OperatingSystem.objects.all()
    asset_collection = Asset.objects.all().order_by('id')

    if operation_system is not None:
        os = get_object_or_404(OperatingSystem, id=int(operation_system))
        asset_collection = asset_collection.filter(os=os)

        return render(request, 'asset/asset/list.html', {
            'os': os,
            'oses': oses,
            'asset_collection': asset_collection,
        })
    else:
        return render(request, 'asset/asset/list.html', {
            'oses': oses,
            'asset_collection': asset_collection,
        })


# Страница актива
@login_required
def AssetDetail(request, id, slug):
    asset = get_object_or_404(Asset, id=id, slug=slug)
    return render(request, 'asset/asset/detail.html', {'asset': asset})


# Список тревог
@login_required
def AlertList(request, asset=None, alert_type=None):
    alerts = Alert.objects.all().order_by('-time')

    if asset is not None:
        alerts = alerts.filter(asset=get_object_or_404(Asset, slug=asset))

    if alert_type is not None:
        alerts = alerts.filter(type=get_object_or_404(AlertType,
                                                      pk=alert_type))

    return render(request, 'asset/alert/list.html', {'alerts': alerts})
