from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'madebynortheastern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'madeby.views.index'),
    url(r'^/$', 'madeby.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)
