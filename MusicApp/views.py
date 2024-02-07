from django.shortcuts import render
from django.http import FileResponse
from .music_protector.music_protector import MusicProtector
# Create your views here.
def music_list(request):
    # Vous devez récupérer une liste de fichiers musicaux à afficher
    music_files = ['file1.enc', 'file2.enc']  # Remplacez par la vraie liste de fichiers

    return render(request, 'music_list.html', {'music_files': music_files})

def download_decrypted_music(request, music_file):
    protector = MusicProtector()
    decrypted_file_path = f'decrypted_{music_file}'
    protector.decrypt_music(music_file, decrypted_file_path)

    response = FileResponse(open(decrypted_file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{decrypted_file_path}"'
    return response