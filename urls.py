from django.conf.urls import patterns, url

from gctest import views, views_api

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^apps/$', views.AppListView.as_view(), name='apps'),
                       url(r'^developers/$', views.DeveloperListView.as_view(), name='developers'),

                       url(r'^app/(?P<app_id>\d+)/$', views.app, name='app'),
                       url(r'^developer/(?P<pk>\d+)/$', views.DeveloperDetailView.as_view(), name='developer'),
                       url(r'^build/(?P<pk>\d+)/$', views.BuildDetailView.as_view(), name='build'),

                       url(r'^app/(?P<app_id>\d+)/edit/$', views.edit_app, name='edit_app'),
                       url(r'^developer/(?P<developer_id>\d+)/edit/$', views.edit_developer, name='edit_developer'),
                       url(r'^build/(?P<build_id>\d+)/edit/$', views.edit_build, name='edit_build'),

                       url(r'^app/(?P<app_id>\d+)/delete/$', views.delete_app, name='delete_app'),
                       url(r'^developer/(?P<app_id>\d+)/delete/$', views.delete_developer, name='delete_developer'),
                       url(r'^build/(?P<app_id>\d+)/delete/$', views.delete_build, name='delete_build'),

                       url(r'^app/new/$', views.new_app, name='new_app'),
                       url(r'^developer/new/$', views.new_developer, name='new_developer'),
                       url(r'^build/new/$', views.new_build, name='new_build'),

                       url(r'^app/api/$', views_api.app_list),
                       url(r'^app/api/$', views_api.build_list),

                       url(r'^app/api/(?P<app_id>\d+)/$', views_api.app_detail),
                       url(r'^build/api/(?P<build_id>\d+)/$', views_api.build_detail),
)
