from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import * 

urlpatterns = [
    
    path('',index,name="index"),
    path('add_book',add_book,name="add_book"),
    path('delete_book/<int:myid>/',delete_book,name="delete_book"),
    path('edit_book/<int:myid>/',edit_book,name="edit_book"),
    path('update_book/<int:myid>/',update_book,name="update_book"),
   
]