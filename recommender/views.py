from django.shortcuts import render, HttpResponse, redirect
from .models import MovieDataBase
from django import forms
from django.contrib import messages
from .forms import MovieRecsInputData

def home(request):
    return render(request, 'recommender/home.html')

def wordcloud(request):
    context = {
        'data': MovieDataBase.objects.all()
    }
    return render(request, 'recommender/wordcloud.html', context)

def movieselection(request):
    context = {} 
    context['form'] = MovieRecsInputData() 
    return render(request, 'recommender/movieselection.html', context)




