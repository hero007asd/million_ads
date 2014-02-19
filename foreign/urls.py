'''
@author: William
'''
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from foreign import views
urlpatterns = patterns('',
#     url(r'^index/$',TemplateView.as_view(template_name='foreign.html')),
    url(r'^index/$',views.inimoney,name='index'),
#     url(r'^loginResult/$',views.login),
    url(r'^login/$',views.mylogin),
    # url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'foreign/login.html'}),
    url(r'^saveorder/$',views.saveOrder),
)