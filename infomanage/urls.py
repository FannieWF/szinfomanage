# -*- coding: utf-8 -*-
# @Author: Fannie
from django.conf.urls import url
from . import views

app_name = 'infomanage'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^bjjydy/$', views.bjjydy, name='bjjydy'),
    url(r'^bjjydy/(?P<article_id>[0-9]+)/rem/$', views.article_rem, name='article_rem'),
    url(r'^bjjydy/(?P<article_id>[0-9]+)/change/$', views.article_change, name='article_change'),
    url(r'^bjjydy/article/batchrem/$', views.article_batch_rem, name='article_batch_rem'),
    url(r'^kt/$', views.kt, name='kt'),
    url(r'^kt/batchrem/$',views.kt_batch_rem, name='kt_batch_rem'),
    url(r'^kt/(?P<kt_id>[0-9]+)/rem/$', views.kt_rem, name='kt_rem'),
    url(r'^kt/(?P<kt_id>[0-9]+)/change/$', views.kt_change, name='kt_change'),
]
