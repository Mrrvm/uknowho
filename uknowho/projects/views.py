from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'	

class LoginView(generic.TemplateView):
	template_name = 'projects/login.html'

class RegisterView(generic.TemplateView):
	template_name = 'projects/register.html'

class DashboardView(generic.TemplateView):
	template_name = 'projects/dashboard.html'

