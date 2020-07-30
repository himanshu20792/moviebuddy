from django import forms
    
movies_choice =( 
    ("The Terminator", "The Terminator"), 
    ("Kindergarden Cop", "Kindergarden Cop"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 

class MovieRecsInputData(forms.Form):
    Choose_Movie = forms.ChoiceField(choices = movies_choice)