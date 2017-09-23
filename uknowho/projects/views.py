from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class ProfileView(generic.TemplateView):
	template_name = 'projects/profile.html'

class ProjectCreate(CreateView):
	model = Project
	fields=['title','description','photo','duration','size','projectType','owner']

class SearchByProjectType(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		return Project.objects.all(projectType=type)
