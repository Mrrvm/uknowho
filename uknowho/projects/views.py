from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'projects/base.html', {})

def detail(request,project_id):
	return HttpResponse("<h2> Details for project"+str(project_id)+"</h2>")

def newProjectForm(request):
	return HttpResponse("<h1> New Project form</h1>")
