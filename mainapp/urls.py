# -*- coding: utf8 -*-
from django.conf.urls import url

from mainapp.views import view_index, view_sign_up, view_sign_in, view_logout, view_write_msg

urlpatterns = [
    url(r'^$', view_index, name='index'),
    url(r'^sign_up/$', view_sign_up, name='sign_up'),
    url(r'^sign_in/$', view_sign_in, name='sign_in'),
    url(r'^logout/$', view_logout, name='logout'),
    url(r'^write_msg', view_write_msg, name='write_msg'),
]
