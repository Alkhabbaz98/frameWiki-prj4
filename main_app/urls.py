from django.urls import path
from . import views

urlpatterns = [
   path('frameWiki/movelist/', views.MoveListView.as_view(), name ='movelist'),
   path('frameWiki/<int:pk>/', views.MoveDetailView.as_view(), name = 'move_details'),
   path('frameWiki/new/', views.MoveCreateView.as_view(), name = 'move_create'),
   path('frameWiki/<int:pk>/edit/', views.MoveUpdateView.as_view(), name='move_update')
]
