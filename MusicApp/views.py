# MusicProtection/MusicApp/views.py

from django.shortcuts import render
from .models import MusicFile
from .music_protector.music_protector import encrypt_music
from django.core.files.uploadedfile import TemporaryUploadedFile
import os

def upload_music(request):
    if request.method == 'POST':
        try:
            music_file= request.FILES['music_file']
            # verifier si le fichier est temporaire
            if isinstance(music_file,TemporaryUploadedFile):
                #chemin du fichier temporaire
                file_path=music_file.temporary_file_path()
                #creation du chemin pour le fichier  chiffré
                encrypted_file_path = 'encrypted_music/'+music_file.name
                #creation de l'objet MusicFile dans la base de données
                MusicFile.objects.create(
                    name=music_file.name,
                    encrypted_file=encrypted_file_path
                )
                #Appel a la fonction de chiffrement
                encrypt_music(file_path)
            else:
                # gerer le cas ou le fichier n'est pas temporaire
                pass
                # fermerture du fichier temporaire
        finally:
                # Supprimer le fichier temporaire
                if 'file_path' in locals() and os.path.exists(file_path):
                    os.remove(file_path)
    return render(request, 'upload_music.html')

def music_list(request):
    music_files = MusicFile.objects.all()
    return render(request, 'music_list.html', {'music_files': music_files})