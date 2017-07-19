from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$',views.contact,name="contact"),
	url(r'^access/$',views.access,name="access"),
	url(r'^log/$',views.log,name="log"),
	url(r'^x/',views.x,name="x"),
	url(r'^forgot/',views.forgot,name="forgot")
]