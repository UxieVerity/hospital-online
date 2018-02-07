from django.conf.urls import url
from . import views


app_name = 'hospital'
urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^table/$', views.table, name='table'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^news/$', views.news, name='news'),
    url(r'^newsdetail/$', views.newsdetail, name='newsdetail'),
    url(r'^adminhandle/$', views.adminhandle, name='adminhandle'),
    url(r'^adminhandled/$', views.adminhandled, name='adminhandled'),
    url(r'^admindown/$', views.admindown, name='admindown'),
    url(r'^admindetail/$', views.admindetail, name='admindetail'),
    url(r'^doctorhandle/$', views.doctorhandle, name='doctorhandle'),
    url(r'^doctorhandled/$', views.doctorhandled, name='doctorhandled'),
    url(r'^doctordetail/$', views.doctordetail, name='doctordetail'),
    url(r'', views.index, name='index'),
]