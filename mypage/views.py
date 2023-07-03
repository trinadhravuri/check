from django.shortcuts import render,redirect
from .models import Skills,Projects
from .forms import EnquiryForm
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    skills = Skills.objects.all()
    skills = skills[:4]
    projects = Projects.objects.all()
    projects = projects[:4]
    form = EnquiryForm
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enquiry submitted successfully.Thank You.I will reply or contact you soon..Good Day.')
            return redirect('enqsuc')
    context ={
        'form':form,
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

def contactme(request):
    form = EnquiryForm
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enquiry submitted successfully.Thank You.I will reply or contact you soon..Good Day.')
            return redirect('enqsuc')
    context ={
        'form':form
    }
    return render(request,'contactme.html',context)

def enqsuccess(request):
    return render(request,'enquirysuccess.html')

def python_dev(request):
    return render(request,'python-development.html')