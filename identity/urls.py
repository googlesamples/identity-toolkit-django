from django.conf.urls import patterns, url

from identity import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^widget$', views.widget, name='widget'),
)