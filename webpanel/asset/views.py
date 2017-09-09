from django.shortcuts import render, get_object_or_404, redirect
from .models import Asset, OperatingSystem
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
def AssetDetail(request, id, slug):
    asset = get_object_or_404(Asset, id=id, slug=slug)
    return render(request, 'asset/asset/detail.html', {'asset': asset})
