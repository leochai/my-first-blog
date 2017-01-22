from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/static/img/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/home/leochai/my-first-blog/blog/static/img'}),
]