from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^invited/$', views.GuestView.as_view(), name="invite"),

]
