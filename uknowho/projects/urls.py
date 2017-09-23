from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
	# /projects/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /login/
    url(r'^login/$', views.LoginView.as_view(), name='login'),

    # /register/
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    # /find/
    url(r'^find/$', views.DashboardView.as_view(), name='find'),


    # /profile/
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    #/createproj/
    url(r'^createproj/$', views.ProjectCreate.as_view(), name="project_add"),

    #/search/hw/
    url(r'^(?P<type>[a-z]{2})/$', views.SearchByProjectType.as_view(),name="search_type"),

    #/123/profile/ (/<user>/profile)
    #url(r'^profile/)
]
