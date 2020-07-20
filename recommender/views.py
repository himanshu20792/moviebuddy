from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'recommender/home.html')

def wordcloud(request):
    return HttpResponse("You're looking at question")
    #return render(request, 'recommender/wordcloud.html')

def movieselection(request):
    return render(request, 'recommender/movieselection.html')

# Create your views here.
