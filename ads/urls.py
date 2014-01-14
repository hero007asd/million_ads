'''
Created on 2013/11/22
@author: William
'''
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from ads import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'million_ads.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$',TemplateView.as_view(template_name='index.html')),
    url(r'^getdetail/$',views.get_dp_detail),
)