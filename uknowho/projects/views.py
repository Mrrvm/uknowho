from django.shortcuts import render
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'


class RegisterView(generic.TemplateView):
	template_name = 'projects/register.html'

class DashboardView(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
<<<<<<< HEAD
		return Project.objects.all()
=======
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
>>>>>>> 1dbc1a97460b9f62191efc866ed1c1fdc9cabd81
