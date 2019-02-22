from django.conf.urls import url
from . import views


app_name = 'post'
urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^create/$', views.create, name='create'),
    url(r'^view/(?P<p_id>[0-9]+)/$', views.detail_post, name='detail'),
]
