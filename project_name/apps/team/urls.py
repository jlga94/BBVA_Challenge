from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^team/$', views.TeamView.as_view(), name="team"),
    url(r'^team-associate/$', views.TeamAssociateView.as_view(), name="team-associate"),

]
