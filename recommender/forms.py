from django import forms
from .models import ContentRec
from django.core.exceptions import ValidationError
    
movies_choice =( 
    ("The Terminator", "The Terminator"), 
    ("Kindergarden Cop", "Kindergarden Cop"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

subtype =(
    ("independent_film", "independent_film"),
    ("murder", "murder"),
    ("based_on_novel", "based_on_novel"),
    ("suspense", "suspense"),
    ("sex", "sex"),
    ("musical", "musical"),
    ("nudity", "nudity"),
    ("love", "love"),
    ("violence", "violence"),
    ("police", "police"),
    ("revenge", "revenge"),
    ("sport", "sport"),
    ("friendship", "friendship"),
    ("female_nudity", "female_nudity"),
    ("world_war_ii", "world_war_ii"),
    ("prison", "prison"),
    ("biography", "biography"),
    ("new_york", "new_york"),
    ("drug", "drug"),
    ("sequel", "sequel"),
    ("los_angeles", "los_angeles"),
    ("paris", "paris"),
    ("dystopia", "dystopia"),
    ("teenager", "teenager"),
    ("rape", "rape"),
    ("serial_killer", "serial_killer"),
    ("gay", "gay"),
    ("london_england", "london_england"),
    ("robbery", "robbery"),
    ("suicide", "suicide"),
    ("high_school", "high_school"),
    ("detective", "detective"),
    ("film_noir", "film_noir"),
    ("jealousy", "jealousy"),
    ("escape", "escape"),
    ("prostitute", "prostitute"),
    ("new_york_city", "new_york_city"),
    ("daughter", "daughter"),
    ("family", "family"),
    ("small_town", "small_town"),
    ("monster", "monster"),
    ("marriage", "marriage"),
    ("lawyer", "lawyer"),
    ("extramarital_affair", "extramarital_affair"),
    ("dying_and_death", "dying_and_death"),
    ("teacher", "teacher"),
    ("island", "island"),
    ("alien", "alien"),
)

popular = [] 
for x in ContentRec.objects.all():
    if float(x.popularity) > 15:
        popular.append(x.title)

#comedy = []
#action = []
#romance = []
#horror = []
#for x in popular:
#    print(ContentRec.objects.filter(title = x).values('genres'))
#    if 'comedy' in ContentRec.objects.filter(title = x).values('genres'):
#        comedy.append(x)
            #if 'action' in y.genres:
            #    action.append(y.title)
            #if 'romance' in y.genres:
            #    romance.append(y.title)
            #if 'horror' in y.genres:
            #    horror.append(y.title)

#print(comedy)

choices = {
    (o.title, str(o)) for o in ContentRec.objects.all()
}

popular = {
    (o, o) for o in popular
}

class MovieInputForm(forms.Form):
    choose_movie = forms.ChoiceField(choices=popular, label = "Choose Movie")
    #choose_movie = forms.CharField()

class WordForm(forms.Form):
    choose_word = forms.ChoiceField(choices=subtype, label = "Choose Word")
