from django.conf.urls import url

from . import views
from .views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^landing/$', views.user_landing_view, name='landing'),
]