
from django.conf.urls import url
#from django.contrib import admin
from river import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
