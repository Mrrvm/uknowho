from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'projects'

urlpatterns = [
	# /projects/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /login/
    url(r'^login/$', auth_views.login, {'template_name': 'projects/login.html'}, name='login'),

    # /logout/
    url(r'^logout/$', auth_views.logout, {'next_page': 'projects/index.html'} ,name='logout'),

    # /register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /dashboard/
    url(r'^dashboard/$', login_required(views.DashboardView.as_view(), login_url='/login/'), name='find'),

    # /profile/
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    #/createproj/
    url(r'^createproj/$', login_required(views.ProjectCreate.as_view(), login_url='/login/'), name="project_add"),

    #/search/hw/
    url(r'^search/(?P<type>[a-z]{2})/$', views.SearchByProjectType.as_view(),name="search_type"),

    #/projects/123/
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.ProjectSubscribe.as_view(),name="projectSubscribe"),
    
]
