from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    # url(r'^wishlist_app/edit/(?P<id>[0-9]+)$', views.edit),
    url(r'^wishlist_app/show/(?P<id>[0-9]+)$', views.show),
    url(r'^wishlist_app/join/(?P<id>[0-9]+)$', views.join),
    url(r'^wishlist_app/remove/(?P<id>[0-9]+)$', views.remove),
    url(r'^wishlist_app/delete/(?P<id>[0-9]+)$', views.delete),
    url(r'^create$', views.createItem),
    url(r'^goback$', views.goback),   
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout),    
]                           
