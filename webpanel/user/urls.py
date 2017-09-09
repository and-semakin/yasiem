from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.ProfileUpdate, name='ProfileUpdate'),
    url(r'^signup/$', views.SignUp, name='SignUp'),
]