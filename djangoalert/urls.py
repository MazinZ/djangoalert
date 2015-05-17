from django.conf.urls import include, url
from django.contrib import admin
from alerts import views as alertview
#from django.contrib import *
from django.contrib.auth import views

from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoalert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^active/', alertview.active, name='active'),
    url(r'^alertjson/', alertview.alert_json, name ='alertjson'),
    url(r'^$', alertview.index),
    #url(r'^$', views.login, {'template_name': 'alerts/index.html'}, name="login"),
    
   # url(r'^logout/$', views.logout, {'template_name': 'alerts/logout.html'}, name="logout"),
    
    
    url(r'^login/$', views.login, {'template_name': "alerts/login.html"}, name="login"),    
    url(r'^logout/$', views.logout, {'next_page': reverse_lazy("login")}, name="logout"),
    
]

