from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
	# /user/
    url(r'^$', views.index, name='index'),
    
]
