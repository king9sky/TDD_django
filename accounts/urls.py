#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Marvin King
# Date     : 2019-02-28 
from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout')
]
