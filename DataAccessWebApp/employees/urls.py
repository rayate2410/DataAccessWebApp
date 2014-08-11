
'''
Created on Jul 30, 2014

@author: rayy
'''
from django.conf.urls import patterns, include, url
import employees.views as login_view

urlpatterns = patterns('',
   
    url(r'^$', login_view.index),
    url(r'^simple_template/$', login_view.template_example),
    url(r'^rendertoresponse/$', login_view.rendertoresponse),
    #url(r'^get/(?P<emp_id>\d+)/$', login_view.get_Employee_details),
    url(r'^get$', login_view.get_Employee_details),
    
    url(r'^getall/$', login_view.get_all),
)
