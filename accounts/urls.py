from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts.views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/accounts/logout/complete/'}, name='logout'),
    url(r'^logout/complete/$', logout_complete),
    url(r'^profile/$', profile, name="profile"),
    url(r'^register/$', register, name='register'),
    url(r'^register/complete/$', registration_complete),
]
