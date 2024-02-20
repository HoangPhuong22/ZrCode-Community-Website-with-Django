from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def paginatorPage(request, profiles, result):
    page = request.GET.get('page')
    paginator = Paginator(profiles, result)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    page = int(page)
    leftIndex = page - 2
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = page + 3
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
    return profiles, range(leftIndex, rightIndex + 1)


def searchProfiles(request):
    search_name = ''
    if request.GET.get('search_name'):
        search_name = request.GET.get('search_name')
    skills = Skill.objects.filter(name__icontains = search_name)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_name) |
        Q(short_intro__icontains=search_name) |
        Q(skill__in=skills))
    
    return profiles, search_name