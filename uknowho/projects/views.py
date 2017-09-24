<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, redirect
from django.template import RequestContext
>>>>>>> df00e207bc766ad03a4cf22f1b0698f85488c330
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




class IndexView(generic.TemplateView):
	template_name = 'projects/index.html'


class LoginView(generic.TemplateView):
	template_name = 'projects/login.html'

#<<<<<<< HEAD
class RegisterView(generic.TemplateView):
	template_name = 'projects/register.html'


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
		message = "Welcome to uknowho\n\nCreate a new " \
				  "project if you have already an idea or " \
				  "find one today!\n\nBest regards,\nuknowho team"
		send_email(email, message)
		return render(request, 'projects/index.html', {'form': form}, RequestContext(request))

		#if form.is_valid():
			#user = form.save(commit=True)
			#username = form.cleaned_data['username']
			#password = form.cleaned_data['password'
			#email = form.cleaned_data['email']
			#user.save()
			#user = authenticate(username=username, password=password)
			#if user.is_active():
				#    login(request, user)
			#return redirect('projects/index.html')
		#return render(request, 'projects/register.html', {'form': form})
'''=======
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
>>>>>>> ead78991a277353678209375944d4cd65a9afbbb'''

@method_decorator(login_required(login_url='/login/'), name = 'dispatch' )
class DashboardView(generic.ListView):
	template_name = 'projects/dashboard.html'
	context_object_name = 'all_projects'

	def get_queryset(self):
<<<<<<< HEAD

=======
>>>>>>> df00e207bc766ad03a4cf22f1b0698f85488c330
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
<<<<<<< HEAD
		return Project.objects.filter(projectType=type)
=======
		return Project.objects.filter(projectType=self.type)
>>>>>>> df00e207bc766ad03a4cf22f1b0698f85488c330
