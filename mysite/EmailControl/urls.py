from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^starttask/$', views.starttask, name='starttask'),
	url(r'^result/(?P<result_code>[0-9]+)/$', views.result, name='result'),
]
