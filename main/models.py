from django.db import models
import datetime

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=200, unique=True)
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.artist

    def __unicode__(self):
        return self.artist

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.CharField(max_length=200, unique=True)
    artist = models.ForeignKey(Artist)
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.album

    def __unicode__(self):
        return self.album

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.CharField(max_length=200)
    lyrics = models.TextField()
    artist = models.ForeignKey(Artist, null=True)
    album = models.ForeignKey(Album, null=True)
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.song
        return self.lyrics

    def __unicode__(self):
        return self.song
        return self.lyrics