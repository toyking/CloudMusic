# -*- coding: utf-8 -*-
from django.conf.urls import url

from NetEaseCloudMusic import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^login', views.login),
]

urlpatterns += [
    url(r'^post/login', views.login_post),
]
