from django.conf.urls import url
from django.contrib import admin
from.import views

app_name= 'purpose'

urlpatterns = [
    url(r'^$',views.section,name="home"),
    url(r'^users$',views.users,name="users"),
    url(r'^delete/list/(?P<pk>[\w-]+)$', views.delete, name='delete'),
    url(r'^updatelist/(?P<pk>[\w-]+)$', views.edit, name='update'),
  	url(r'^retrivelist/(?P<pk>[\w-]+)$', views.retrieve_user_list, name='retrive_user_list'),

    #url(r'^$',views.login_view,name="login"),
    #url(r'^logout/$',views.logout_view,name="logout"),

]
