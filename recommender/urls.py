"""movierecs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'recommender-home'),
    path('wordcloud/', views.wordselection, name = 'recommender-wordcloud'),
    path('wordcloud/<int:my_id>/', views.wordcloud_detail, name = 'recommender-wordcloud'),
    path('movieselection/', views.movieselection, name = 'recommender-movieselection'),
    path('movieselection/output', views.output),
    path('upload-csv/', views.contact_upload, name = "contact_upload"),
]
