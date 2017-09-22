from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
	# /projects/
    url(r'^$', views.index, name='index'),
    #/projects/12345/
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    #/projects/newProjectForm/
    url(r'^projects/newProjectForm$',views.newProjectForm, name='newProjectForm'),

]
