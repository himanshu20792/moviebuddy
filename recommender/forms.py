from django import forms
from django.core.exceptions import ValidationError
    
movies_choice =( 
    ("The Terminator", "The Terminator"), 
    ("Kindergarden Cop", "Kindergarden Cop"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

subtype =(
    ("Independent Film","Independent Film"),
    ("Murder","Murder"),
    ("Based On Novel","Based On Novel"),
    ("Suspense","Suspense"),
    ("sex","sex"),
    #musical,nudity,love,violence,police,revenge,sport,friendship,female_nudity,world_war_ii,prison,biography,new_york,drug,sequel,los_angeles,paris,dystopia,teenager,rape,serial_killer,gay,london_england,robbery,suicide,high_school,detective,film_noir,jealousy,escape,prostitute,new_york_city,daughter,family,small_town,monster,marriage,lawyer,extramarital_affair,dying_and_death,teacher,island,alien,hospital
)

class MovieInputForm(forms.Form):
    choose_movie = forms.CharField()
