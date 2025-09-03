from django.urls import path
from . import views

urlpatterns = [
   path('frameWiki/',views.MoveListView.as_view(), name ='movelist')
]
