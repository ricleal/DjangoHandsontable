from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    # /app1
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.DataListView.as_view(), name='list'),
    url(r'^create/$', views.create_data_ajax, name='create'),
    url(r'^form/$', views.DataFormView.as_view(), name='form'),
    ## Reduction inline formset
    url(r'^reduction/$', views.CreateReductionView.as_view(), name='reduction_new'),
    url(r'^reduction/(?P<pk>\d+)/$', views.UpdateReductionView.as_view(), name='reduction_update'),
]
