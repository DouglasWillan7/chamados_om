from django.conf.urls import patterns, url

from setores import views

urlpatterns = patterns('',
  url(r'^$', views.SetorList.as_view(), name='setor_list'),
  url(r'^new$', views.SetorCreate.as_view(), name='setor_new'),
  url(r'^edit/(?P<pk>\d+)$', views.SetorUpdate.as_view(), name='setor_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.SetorDelete.as_view(), name='setor_delete')
)
