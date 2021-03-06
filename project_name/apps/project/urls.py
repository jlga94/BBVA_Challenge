from django.conf.urls import url

from . import views

urlpatterns = [
	#'project.views',
    url(r'^project/$', views.ProjectView.as_view(), name="project"),
    url(r'^project/save/dg$', views.save_datos_generales, name="save_datos_generales"),
    url(r'^project-list/$', views.ProjectListView.as_view(), name="project-list"),
    url(r'^lista-pagos/$', views.PagosListView.as_view(), name="pagos-list"),
    url(r'^project-detail/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail'), 
    url(r'^project-list/(?P<pk>[0-9]+)/results/$', views.ProjectResultsView.as_view(), name="project-result"),
    url(r'^vista-pagos/$', views.VistaPagosListView.as_view(), name="vista-pagos"),   
    url(r'^detalle-pago/$', views.DetallePagosListView.as_view(), name="detalle_pago"),   
]
