from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chamados_om.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
)
