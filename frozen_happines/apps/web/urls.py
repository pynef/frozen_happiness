#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('frozen_happines.apps.web.views',
	url(r'^$','web',name='web'),
)
