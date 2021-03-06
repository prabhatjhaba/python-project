from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.edit_post, name='edit_post'),
]
