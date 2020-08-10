from django.shortcuts import render, HttpResponse, redirect
from .models import MovieDataBase, ContentRec
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MovieInputForm
from django.contrib import messages
from recommender.utils import rec
import csv, io 
from django.contrib.auth.decorators import permission_required

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
            fieldout = rec(field)
            #messages.success(request,f'You choose {field}!')
            request.session['field'] = field
            request.session['fieldout'] = fieldout
            return HttpResponseRedirect('/movieselection/output')
    else: 
        form = MovieInputForm() 
    return render(request, 'recommender/movieselection.html', {'form':form})

def output(request):
    field = request.session['field']
    fieldout = request.session['fieldout']
    out = {"name" : field, "recommendations" : fieldout}
    return render(request, 'recommender/movieselection_detail.html', out)

@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = "recommender/contact_upload.html"
    prompt = {
        'order': 'Order of the CSV should be id, title, tagline, description, genres, keywords, date, collection, runtime, revenue_budget, director, cast, production_companies, production_countries, popularity, average_vote, num_votes, language, imdb_id, poster_url'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ',', quotechar = "|"):
        print(column[0])
        print(column[1])
        print(column[2])
        print(column[3])
        print(column[4])
        print(column[5])
        print(column[6:])
        print('_____________________')
        _, created = ContentRec.objects.update_or_create(
            id1 = column[0], 
            title = column[1], 
            popularity = column[2],
            average_vote = column[3], 
            num_votes = column[4], 	
            keywords = column[5:],
        )
    context = {} 
    return render(request, template, context)

