from django.db import models

# Create your models here.
class MusicFile(models.Model):
    name = models.CharField(max_length=100)
    encrypted_file = models.FileField(upload_to='encrypted_music/')

    class Meta:
        app_label = 'MusicApp'