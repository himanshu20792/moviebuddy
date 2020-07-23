from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'recommender/home.html')

def wordcloud(request):
    return render(request, 'recommender/wordcloud.html')

def movieselection(request):
    return render(request, 'recommender/movieselection.html')


