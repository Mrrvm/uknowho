from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Project

# Create your views here.
def index(request):
	all_projects=Project.objects.all()
	template = loader.get_template('projects/index.html')	

	return render(request, 'projects/base.html', {})

def detail(request,project_id):
	return HttpResponse("<h2> Details for project"+str(project_id)+"</h2>")

def newProjectForm(request):
	return HttpResponse("<h1> New Project form</h1>")
