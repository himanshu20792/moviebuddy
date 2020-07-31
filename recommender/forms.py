from django import forms
from django.core.exceptions import ValidationError
    
movies_choice =( 
    ("The Terminator", "The Terminator"), 
    ("Kindergarden Cop", "Kindergarden Cop"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class MovieRecsInputData(forms.Form):
    choose_movie = forms.ChoiceField(label='Choose Movie', choices = movies_choice)

    