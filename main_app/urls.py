from django.urls import path
from . import views

urlpatterns = [
   path('frameWiki/movelist/', views.MoveListView.as_view(), name ='movelist'),
   path('frameWiki/<int:pk>/', views.MoveDetailView.as_view(), name = 'move_details'),
   path('frameWiki/new/', views.MoveCreateView.as_view(), name = 'move_create'),
   path('frameWiki/<int:pk>/edit/', views.MoveUpdateView.as_view(), name='move_update'),
   path('frameWiki/<int:pk>/delete/', views.MoveDeleteView.as_view(), name = 'move_delete'),
   path('frameWiki/games/', views.list_all_games, name = 'gamelist'),
   path('frameWiki/games/<int:game_id>/', views.character_list, name = 'characterlist'),
   path('frameWiki/characters/<int:character_id>/', views.character_details, name = 'character_details')
]
