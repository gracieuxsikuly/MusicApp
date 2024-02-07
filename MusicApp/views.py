# MusicProtection/MusicApp/views.py

from django.shortcuts import render
from .models import MusicFile
from .music_protector.music_protector import encrypt_music

def upload_music(request):
    if request.method == 'POST':
        music_file = request.FILES['music_file']
        encrypted_file_path = 'encrypted_music/' + music_file.name
        MusicFile.objects.create(name=music_file.name, encrypted_file=encrypted_file_path)
        encrypt_music(music_file.temporary_file_path())
    
    return render(request, 'upload_music.html')
def music_list(request):
    music_files = MusicFile.objects.all()
    return render(request, 'music_list.html', {'music_files': music_files})