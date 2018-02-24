from django.conf.urls import url
from .views import index,about

urlpatterns = [
	url(r'^$', index),
	url(r'^about/$', about),
]