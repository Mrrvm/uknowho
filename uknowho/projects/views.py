from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'

class RegisterView(generic.TemplateView):
	template_name = 'projects/register.html'

class DashboardView(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		return Project.objects.all()

class ProfileView(generic.TemplateView):
	template_name = 'projects/profile.html'

@method_decorator(login_required(login_url='/login/'), name = 'dispatch' )
class ProjectCreate(CreateView):
	model = Project
	fields=['title','description','photo','duration','size','projectType','owner']

class SearchByProjectType(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		return Project.objects.all(projectType=type)

class UserFormView(View):
	form_class = UserForm
	template_name = 'projects/register.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form}, RequestContext(request))

	def post(self, request):
		form = self.form_class(request.POST)
		username = request.POST.get['username', False]
		password = request.POST.get['password', False]		
		email = request.POST.get['email', False]
		user = User.objects.create_user(username, email, password)
		user.save()
		return render(request, 'projects/index.html', {'form', form}, RequestContext(request))

	 	
