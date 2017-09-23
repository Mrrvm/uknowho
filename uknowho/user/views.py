from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Profile

# Create your views here.
def index(request):
	return HttpResponse("<h1>Your mom is hot</h1>")



# Create your views here.

class IndexView(generic.ListView):
	template_name = 'user/index.html'

	def get_queryset(self):
		return Profile.objects.all()

class DetailView(generic.DeleteView):
	model = Profile
	template_name = 'user/detail.html'

class UserCreate(CreateView):
	model = Profile
	fields = ['first_name', 'last_name', 'country', 'city', 'course', 'university', 'phoneNumber', 'linkedIn', 'facebook', 'twitter', 'photo']

class UserUpdate(UpdateView):
	model = Profile
	fields = ['first_name', 'last_name', 'country', 'city', 'course', 'university', 'phoneNumber', 'linkedIn', 'facebook', 'twitter', 'photo']

class UserDelete(DeleteView):
	model = Profile
	success_url = reverse_lazy('projects:index')