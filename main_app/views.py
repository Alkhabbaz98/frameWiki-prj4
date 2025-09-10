from django.shortcuts import render
from .models import Game 
from .models import Character
from .models import Move

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Game, Character, Move
from . form import MoveForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


class MoveDetailView(LoginRequiredMixin, DetailView):
    model = Move
    template_name = 'move_details.html'
    context_object_name = 'move'

class MoveCreateView(LoginRequiredMixin, CreateView):
    model = Move
    form_class = MoveForm
    template_name = 'move_form.html'

    def  get_success_url(self):
        character_id = self.object.character_id
        return reverse('character_details', kwargs={"character_id": character_id})
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(form.errors.as_json())
        return response
    def form_valid(self, form):

        return super().form_valid(form)
    

class MoveUpdateView(LoginRequiredMixin, UpdateView):
    model = Move
    form_class = MoveForm
    template_name = 'move_form.html'

    def get_success_url(self):
        return reverse('move_details', kwargs={"pk": self.object.pk})

class MoveDeleteView(LoginRequiredMixin, DeleteView):
    model = Move

    def get_success_url(self):
        character_id = self.object.character.id 
        return reverse_lazy('character_details', kwargs={"character_id": character_id})


@login_required
def list_all_games(request):
    games = Game.objects.all()
    return render(request, 'gamelist.html', {'games': games})


@login_required
def character_list(request, game_id):
    characters = Character.objects.all().filter(game = game_id)
    return render(request, 'characterlist.html', {'characters': characters})

@login_required
def character_details(request,character_id):
    moves = Move.objects.all().filter(character = character_id)
    character = Character.objects.get(id = character_id)
    return render(request, 'character_details.html', {'character': character, 'moves':moves })

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login") 


