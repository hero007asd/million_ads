from django.conf.urls import patterns, include, url

from django.contrib import admin
from million_ads import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'million_ads.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ads/', include('ads.urls',namespace='ads')),
    url(r'^foreign/', include('foreign.urls',namespace='foreign')),
    ('^site_media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATICFILES_DIRS}),
)
