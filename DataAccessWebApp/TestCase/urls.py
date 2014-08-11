
from django.conf.urls import patterns, include, url
import TestCase.views as tc_view
from DataAccessWebApp import settings
from django.conf.urls.static import static
from TestCase.api import TestCaseResource


tc_resource = TestCaseResource()

urlpatterns = patterns('',
   
    url(r'^$', tc_view.index),
   
    url(r'^addTestCase/$', tc_view.add_testcase),
    url(r'^added/$', tc_view.added),
    url(r'^all/$', tc_view.all),
    url(r'^get/(?P<tc_id>\d+)/$', tc_view.get_tc_detail),
    url(r'^status/(?P<tc_id>\d+)$', tc_view.change_status),
    url(r'^tc_search/$', tc_view.search_tc),
    url(r'^search/$', tc_view.search),
    url(r'^api/', include(tc_resource.urls)),
   
)