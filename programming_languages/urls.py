from django.conf.urls import url

from . import views

app_name = 'programming_languages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]
