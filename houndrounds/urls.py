from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from houndroundsapp import views

urlpatterns = patterns('',
    url(r'^houndrounds/', include('houndroundsapp.urls')),                           
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
)
