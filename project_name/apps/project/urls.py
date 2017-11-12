from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/$', views.ProjectView.as_view(), name="project"),
    url(r'^project/save/dg$', views.save_datos_generales, name="save_datos_generales"),
    url(r'^project-list/$', views.ProjectListView.as_view(), name="project-list"),
]
