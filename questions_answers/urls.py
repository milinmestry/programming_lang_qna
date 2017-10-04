from django.conf.urls import url

from . import views

app_name = 'qa_url'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<plid>[0-9]+)/$', views.details, name='details'),
    # url(r'^(?P<plid>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]
