from django.shortcuts import render
from .models import Skills,Projects
# Create your views here.

def base(request):
    return render(request,'base.html')

def allskills(request):
    skills = Skills.objects.all()
    context= {
        'skills':skills
    }
    return render(request,'allskills.html',context)

def allprojects(request):
    projects = Projects.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'allprojects.html',context)