from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name='projects'),
    path('detail-project/<str:pk>/', views.detailProject, name='detail_project'),
    
    path('create-project/', views.createProject, name='create_project'),
    path('update-project/<str:pk>/', views.updateProject, name='update_project'),
    path('delete-project/<str:pk>/', views.deleteProject, name='delete_project'),
]