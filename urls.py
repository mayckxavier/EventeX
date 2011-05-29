# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from route import route #route.py deve ficar no diretório eventex
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
#	(r'^$','core.views.homepage'),
#	url(r'^$',homepage, {'template': 'index.html'}),
	(r'^$','direct_to_template',{'template':'index.html'}),
	(r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

def homepage(request, template=None): #Unpacking do dict
	return render_to_response(template, RequestContext(request))

urlpatterns += staticfiles_urlpatterns()
