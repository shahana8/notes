"""
URL configuration for NotesApp project.

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
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.myNote, name="frontpage"),
    path('notes/<str:pk>/', views.singleNote, name="viewpage"),
    path('create-notes/', views.createNote, name="createnote"),
    path('update-notes/<str:pk>/', views.updateNote, name="updatenote"),
    path('delete-notes/<str:pk>/', views.deleteNote, name="deletenote"),

]
