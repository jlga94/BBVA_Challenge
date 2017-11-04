from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dataset/$', views.DataSetView.as_view(), name="dataset"),
    url(r'^dataset-list/$', views.DataSetListView.as_view(), name="dataset-list"),

]
