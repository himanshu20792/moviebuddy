from django.shortcuts import render, HttpResponse, redirect
from .models import MovieDataBase, ContentRec
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MovieInputForm, WordForm
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

def wordselection(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            field = data['choose_word']
            print(MovieDataBase.objects.get(word = field).id)
            return HttpResponseRedirect('/wordcloud/'+str(MovieDataBase.objects.get(word = field).id))
    else: 
        form = WordForm() 
    return render(request, 'recommender/wordcloud.html', {'form': form})

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
            if ContentRec.objects.filter(title = field).exists():
                fieldout = rec(field)
            else: 
                fieldout = "Movie Name Not Found"
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
        'order': 'Order of the CSV should be'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ';', quotechar = "|"):
        print(column)
        _, created = ContentRec.objects.update_or_create(
            title = column[0],
            genres = column[1], 
            #keywords = ', '.join(column[1:]).replace('"', ''),
            keywords = column[2],	
            popularity = column[3],
            average_vote = column[4],	
            num_votes = column[5],
            )
    context = {} 
    return render(request, template, context)

#filter models to delete anything that has " in title
#seperator sep = ';'