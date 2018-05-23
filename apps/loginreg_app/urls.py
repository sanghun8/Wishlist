from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processReg$', views.processReg),
    url(r'^processLogin$', views.processLogin),
    url(r'^logout$', views.logout),
]