from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [

	url(r'^$',views.index,name='index'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^login/$', auth_views.login),
    url(r'^create/$',views.create, name='create'),
]
