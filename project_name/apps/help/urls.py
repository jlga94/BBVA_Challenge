from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^help/$', views.HelpView.as_view(), name="help"),
    url(r'^help-list/$', views.HelpListView.as_view(), name="help-list"),
]
