from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.AssetList, name='AssetList'),
    url(r'^(?P<operation_system>\d+)/$',
        views.AssetList, name='AssetListByCategory'),
    url(r'^(?P<slug>[-\w]+)/(?P<id>\d+)/$',
        views.AssetDetail, name='AssetDetail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
