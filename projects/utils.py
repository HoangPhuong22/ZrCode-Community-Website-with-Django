from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatorPage(request, projects, result):
    page = request.GET.get('page')
    paginator = Paginator(projects, result)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    page = int(page)
    leftIndex = page - 3
    if leftIndex < 1:
        leftIndex =1
    rightIndex = page + 3
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    return projects, range(leftIndex, rightIndex + 1)

def searchProjects(request):
    search_name = ''
    if request.GET.get('search_name'):
        search_name = request.GET.get('search_name')
        
    tags = Tag.objects.filter(name__icontains=search_name)
    
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_name)|
        Q(description__icontains=search_name)|
        Q(tags__in= tags)|
        Q(owner__name__icontains=search_name)
    )
    return projects, search_name
    