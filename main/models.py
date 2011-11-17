from django.db import models
import datetime

class Lyrics (models.Model):
    id          = models.AutoField(primary_key=True)
    artist      = models.CharField(max_length=200, unique=True)
    song        = models.CharField(max_length=200)
    lyrics      = models.TextField()
    modified    = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Lyrics, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
        return self.song
        return self.lyrics

    def __unicode__(self):
        return self.name
        return self.song
        return self.lyrics