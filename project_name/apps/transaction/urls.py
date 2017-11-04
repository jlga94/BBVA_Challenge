from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^transaction/$', views.TransactionView.as_view(), name="transaction"),
    url(r'^transaction-associate/$', views.TransactionAssociateView.as_view(), name="transaction"),

]
