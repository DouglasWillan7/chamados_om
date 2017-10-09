from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chamados_om.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('perfis.urls')),
    url(r'^', include('usuarios.urls')),
    url(r'^setores/', include('setores.urls')),
    url(r'^chamados/', include('chamados.urls')),
)
