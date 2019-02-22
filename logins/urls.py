from django.conf.urls import url
from . import views


app_name = 'login'
urlpatterns = [
    url(r'^$', views.LogIn, name='login'),
    url(r'^register$', views.Register, name='reg'),
    url(r'^logout$', views.LogOut, name='logout')
]
