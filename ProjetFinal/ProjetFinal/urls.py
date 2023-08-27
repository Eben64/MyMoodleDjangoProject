"""
URL configuration for ProjetFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProjetApp import views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', include('ProjetApp.urls')),
    path('adminDashbord/', views.homeAdmin, name ='admindash'),
    path('teacherDashbord', views.homeTeacher, name='teacherdash'),
    path('studentDashbord', views.homeStudent,  name='studentdash'),
    path('adminLogin', views.adminLogin,  name='adminlogin'),
    path('upload/', views.upload_project, name='upload_project'),
    path('manage/', views.manage_projects, name='manage_projects'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('upload_teacher/', views.upload_project_teacher, name='upload_project_teacher'),
    path('my_projects_teacher/', views.my_projects_teacher, name='my_projects_teacher'),
    path('my_projects_student/', views.my_projects_student, name='my_projects_student'),
    path('submit_project/<int:project_id>/', views.submit_project, name='submit_project'),
    path('archived_projects/', views.archived_projects, name='archived_projects'),
    path('download_project/<int:project_id>/', views.download_project, name='download_project'),

]

