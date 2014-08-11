from django.conf.urls import patterns, include, url
from django.contrib import admin
from DataAccessWebApp import settings
admin.autodiscover()

import views


urlpatterns = patterns('',

    url(r'admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^employees/', include('employees.urls')),
    url(r'^login/', views.login),
    url(r'^auth/', views.auth_view),
    url(r'^profile/', views.profile),
    url(r'^invalid/', views.invalid),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register_view),
    url(r'^registered/', views.registered_view),
    url(r'^testcase/', include('TestCase.urls')),
    
    
)

urlpatterns += patterns('',         
        (r'^static/(?P<path>.*)$', 'django.views.static.serve')
)

