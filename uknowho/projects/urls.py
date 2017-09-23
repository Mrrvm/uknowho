from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
	# /projects/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /login/
    url(r'^login/$', views.LoginView.as_view(), name='login'),

    # /register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /find/
    url(r'^find/$', views.DashboardView.as_view(), name='find'),
]
