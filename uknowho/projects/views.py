from django.shortcuts import render, redirect, get_object_or_404
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
from .send_email import send_email
from projects.choices import *

class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'


class LoginView(generic.TemplateView):
	template_name = 'projects/login.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'projects/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form}, RequestContext(request))

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        form = self.form_class(request.POST)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('projects:index')

        return render(request, 'projects/index.html', {'form': form}, RequestContext(request))

@method_decorator(login_required(login_url='/login/'), name = 'dispatch' )
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
	model = Project
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
		projtype = self.kwargs['type']
		return Project.objects.filter(projectType=projtype)

class ProjectSubscribe(generic.ListView):
	model = Project
	template_name = 'projects/index.html'

	def get_queryset(self):
		projectID = self.kwargs['project_id']

		username = self.request.user.username
		email = self.request.user.email

		print("username" + username)

		print("project ID is " + projectID)

		project = Project.objects.get(pk=projectID)

		send_email(project.owner.email, username, email, project.title)

		return redirect('projects:index')


