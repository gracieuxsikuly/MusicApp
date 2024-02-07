# MusicApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
   # path('music-list/', views.music_list, name='music_list'),
   #  path('download/<str:music_file>/', views.download_decrypted_music, name='download_decrypted_music'),
   path('upload/', views.upload_music, name='upload_music'),
   path('music-list/', views.music_list, name='music_list'),  # URL pour afficher la liste de musique
]