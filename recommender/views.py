from django.shortcuts import render, HttpResponse, redirect
from .models import MovieDataBase
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MovieRecsInputData

def home(request):
    return render(request, 'recommender/home.html')

def wordcloud(request):
    context = {
        'data': MovieDataBase.objects.all()
    }
    return render(request, 'recommender/wordcloud.html', context)

def movieselection(request):
    if request.method == 'POST':
        form = MovieRecsInputData(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['choose_movie']
            print(field)
            return HttpResponseRedirect('/')
    else: 
        context = {} 
        context['form'] = MovieRecsInputData() 
    return render(request, 'recommender/movieselection.html', context)






