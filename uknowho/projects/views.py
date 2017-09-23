from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'projects/index.html'


class LoginView(generic.TemplateView):
    template_name = 'projects/login.html'


class RegisterView(generic.TemplateView):
    template_name = 'projects/register.html'


class DashboardView(generic.TemplateView):
    template_name = 'projects/dashboard.html'


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
        return render(request, 'projects/index.html', {'form': form}, RequestContext(request))
        #if form.is_valid():
            #user = form.save(commit=True)
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            #email = form.cleaned_data['email']
            #user.save()
            #user = authenticate(username=username, password=password)
            #if user.is_active():
            #    login(request, user)
            #return redirect('projects/index.html')
        #return render(request, 'projects/register.html', {'form': form})
