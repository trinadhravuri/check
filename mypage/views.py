from django.shortcuts import render
from .models import Skills,Projects
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    skills = Skills.objects.all()
    skills = skills[:4]
    projects = Projects.objects.all()
    projects = projects[:4]
    context = {
        'skills':skills,
        'projects':projects
    }
    return render(request,'home.html',context)

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

def singleskill(request,pk):
    skill = Skills.objects.get(pk = pk)
    context = {
        'skill':skill
    }
    return render(request,'singleskill.html',context)

def singleproject(request,pk):
    project = Projects.objects.get(pk=pk)
    skills = project.project_skills.all()
    context = {'project':project,'skills':skills}
    return render(request,'singleproject.html',context)