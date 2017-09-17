from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # активы
    url(r'^$', views.AssetList, name='AssetList'),
    url(r'^assets/$', views.AssetList, name='AssetList'),
    url(r'^assets/os/(?P<os_id>\d+)/$',
        views.AssetList, name='AssetListByOs'),
    url(r'^assets/user/(?P<user_id>\d+)/$',
        views.AssetList, name='AssetListByUser'),
    url(r'^assets/os/(?P<os_id>\d+)/user/(?P<user_id>\d+)/$',
        views.AssetList, name='AssetListByOsAndUser'),
    url(r'^assets/details/(?P<slug>[-\w]+)/(?P<id>\d+)/$',
        views.AssetDetail, name='AssetDetail'),

    # тревоги
    url(r'^alerts/$', views.AlertList, name='AlertList'),
    url(r'^alerts/asset/(?P<asset_slug>[-\w]+)/$', views.AlertList,
        name='AlertListForAsset'),
    url(r'^alerts/type/(?P<alert_type_id>\d+)/$',
        views.AlertList, name='AlertListForType'),
    url(r'^alerts/asset/(?P<asset_slug>[-\w]+)/type/(?P<alert_type_id>\d+)/$',
        views.AlertList, name='AlertListForAssetAndType'),
    url(r'^alerts/details/(?P<alert_id>\d+)$', views.AlertDetails,
        name='AlertDetails')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
