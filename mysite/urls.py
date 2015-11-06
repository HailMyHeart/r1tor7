from django.conf.urls import patterns, include, url
from books import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', views.searchAndAdd),
                       (r'^search_result/$', views.search_result),
                       (r'^books/(\w*)$', views.show_book),
                       (r'^update/(\w*)$', views.update_book),
                       (r'^delete/(\w*)$', views.delete),
                       (r'^successful/$', views.successful),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
