from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'

class LoginView(generic.TemplateView):
	template_name = 'projects/login.html'

class RegisterView(generic.TemplateView):
	template_name = 'projects/register.html'

class DashboardView(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		return Project.objects.all()
