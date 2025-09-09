from django.shortcuts import render
from .models import Game 
from .models import Character
from .models import Move

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Game, Character, Move
from . form import MoveForm
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


class MoveListView(ListView):
    model = Move
    template_name = 'movelist.html'
    context_object_name = 'moves'

class MoveDetailView(DetailView):
    model = Move
    template_name = 'move_details.html'
    context_object_name = 'move'

class MoveCreateView(CreateView):
    model = Move
    form_class = MoveForm
    template_name = 'move_form.html'

    def  get_success_url(self):
        return reverse('move_details', kwargs={"pk": self.object.pk})
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(form.errors.as_json())
        return response
    def form_valid(self, form):

        return super().form_valid(form)
    

class MoveUpdateView(UpdateView):
    model = Move
    form_class = MoveForm
    template_name = 'move_form.html'

    def get_success_url(self):
        return reverse('move_details', kwargs={"pk": self.object.pk})

class MoveDeleteView(DeleteView):
    model = Move
    # success_url = 'movelist'
    def get_success_url(self):
        return reverse_lazy('movelist')


def list_all_games(request):
    games = Game.objects.all()
    return render(request, 'gamelist.html', {'games': games})

def character_list(request, game_id):
    characters = Character.objects.all().filter(game = game_id)
    return render(request, 'characterlist.html', {'characters': characters})

def character_details(request,character_id):
    moves = Move.objects.all().filter(character = character_id)
    character = Character.objects.get(id = character_id)
    return render(request, 'character_details.html', {'character': character, 'moves':moves })

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # or your home

