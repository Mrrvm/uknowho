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
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    # /find/
    url(r'^find/$', login_required(views.DashboardView.as_view(), login_url='/login/'), name='find'),

    # /profile/
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    #/createproj/
    url(r'^createproj/$', views.ProjectCreate.as_view(), name="project_add"),

    #/search/hw/
    url(r'^(?P<type>[a-z]{2})/$', views.SearchByProjectType.as_view(),name="search_type"),

    #/123/profile/ (/<user>/profile)
    #url(r'^profile/)
]
