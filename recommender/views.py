from django.shortcuts import render, HttpResponse, redirect
from .models import MovieDataBase
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MovieInputForm
from django.contrib import messages

def home(request):
    return render(request, 'recommender/home.html')

def wordcloud(request):
    context = {
        'data': MovieDataBase.objects.all()
    }
    return render(request, 'recommender/wordcloud.html', context)

def wordcloud_detail(request, my_id):
    obj = MovieDataBase.objects.get(id=my_id)
    context = {
        'data': obj
    }
    return render(request, 'recommender/wordcloud_detail.html', context)    

def movieselection(request):
    if request.method == 'POST':
        form = MovieInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['choose_movie']
            print(field)
            messages.success(request,f'You choose {field}!')
            return HttpResponseRedirect('/')
    else: 
        form = MovieInputForm() 
    return render(request, 'recommender/movieselection.html', {'form':form})






