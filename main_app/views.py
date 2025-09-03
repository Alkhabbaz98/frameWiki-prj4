from django.shortcuts import render
from .models import Game 
from .models import Character
from .models import Move

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Game, Character, Move
# Create your views here.

class MoveListView(ListView):
    model = Move
    template_name = './movelist.html'
    context_object_name = 'moves'

class MoveDetailView(DetailView):
    model = Move
    template_name = './move_details.html'
    context_object_name = 'move'

class MoveCreateView(CreateView):
    model = Move
    fields = ['character','name','move_type','damage','guard_type','start_up','active','recovery','description']
    template_name = './move_form.html'

    def  get_success_url(self):
        return reverse('move_details', kwargs={"pk": self.object.pk})
    
