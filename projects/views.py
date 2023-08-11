from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


# projectslist = [
#     {
#         'id':'1',
#         'title':'ecommerce website',
#         'description':'fully functional'
#
#     },
#     {
#         'id':'2',
#         'title':'prtfolio website',
#         'description':'portfolio building main functional'
#     },
#     {
#         'id':'3',
#         'title':'social network website',
#         'description':'open source functional'
#     }
# ]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    # print('projectObj:',projectObj)
    # projectObj = None
    # for i in projectslist:
    #     if i['id'] == pk:
    #         projectObj = i
    return render(request, 'projects/single-project.html',
                   {'project' : projectObj, 'tags':tags})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form' : form}
    return render(request, "projects/project_form.html",context)


def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')


    context = {'form' : form}
    return render(request, "projects/project_form.html",context)


def deleteProject(request, pk):
    project= Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'projects/delete_object.html',context)