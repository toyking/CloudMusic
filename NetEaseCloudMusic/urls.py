# -*- coding: utf-8 -*-
from django.conf.urls import url

from NetEaseCloudMusic import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^home', views.home),
    url(r'^login', views.login),
    url(r'^top_mv', views.top_mv),
    url(r'^mv_detail', views.mv_detail),
    url(r'^', views.index)
]

urlpatterns += [
    url(r'^post/login', views.login_post),
]
