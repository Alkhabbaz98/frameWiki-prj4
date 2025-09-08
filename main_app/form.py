from django import forms 
from .models import Game, Character, Move

class MoveForm(forms.ModelForm):
    
    class Meta:
        model = Move
        fields = ['image','character','name','move_type','damage','guard_type','start_up','active','recovery','onhit','onblock','description']