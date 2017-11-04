from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/$', views.IndexView.as_view(), name="index"),
    url(r'^user-profile/(?P<uuid>[0-9A-Za-z\-]+)/$', views.UserProfileView.as_view(), name="profile"),
    url(r'^user-change-password/$', views.UserChangePasswordView.as_view(), name="change-password"),
    url(r'^user-coin-kas/$', views.UserCoinKasView.as_view(), name="coin-kas"),
    url(r'^user-invited/$', views.UserInvitedView.as_view(), name="invited"),
    url(r'^user-code-company/$', views.UserCodeCompanyView.as_view(), name="code-company"),
    url(r'^user-company/$', views.UserCompanyView.as_view(), name="company"),
    url(r'^user-company-tree/$', views.UserCompanyTreeView.as_view(), name="company-tree"),
]
