from django.shortcuts import render, redirect
from .forms import ProjectForm, ReviewForm
from .models import Project, Tag
from .utils import searchProjects, paginatorPage
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
# Create your views here.

def projects(request):
    projects, search_name = searchProjects(request)
    projects, custom = paginatorPage(request, projects, 6)  
    context = {'projects': projects, 'search_name': search_name, 'custom': custom}
    return render(request, 'projects/projects.html', context)

def detailProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            
            project.getVoteCount
            
            messages.success(request, 'Your review was successfully submitted.')
            return redirect('detail_project', pk = project.id)
            
            
    context = {'project': project, 'form': form}
    return render(request, 'projects/detail_project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag = tag.capitalize()
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('user_account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag = tag.capitalize()
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
                
            return redirect('user_account')
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('user_account')
    context = {'object': project}
    return render(request, 'delete.html', context)