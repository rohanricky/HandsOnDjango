from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.access, name='access'),
	url(r'^thanks/$',views.thanks, name="thanks"),
	url(r'^x/$',views.x,name="x"),
	url(r'^login/$',views.login,name="login"),
	url(r'^contact/',views.contact, name='contact')
]