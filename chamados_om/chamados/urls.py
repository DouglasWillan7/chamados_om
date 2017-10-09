from django.conf.urls import patterns, url

from chamados import views

urlpatterns = patterns('',
  url(r'^$', views.ChamadoList.as_view(), name='chamado_list'),
  url(r'^new$', views.ChamadoCreate.as_view(), name='chamado_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ChamadoUpdate.as_view(), name='chamado_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ChamadoDelete.as_view(), name='chamado_delete'),
  url(r'^res/(?P<pk>\d+)$', views.ChamadoRes.as_view(), name='chamado_res')
)
