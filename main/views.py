from django.shortcuts import *
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from main.forms import *

WEBSITE_NAME = "Lyricsy - the best place to share, translate, discover new lyrics on the web"

def main(request):
    title = "Main Windfsdfsdsfow"
    songs = Song.objects.order_by('rating')[:10]
    album = Album.objects.order_by('rating')[:10]
    artist = Artist.objects.order_by('rating')[:10]
    return render_to_response('main.html', {
        "title": title,
        "album": album,
        "songs": songs,
        "artist": artist,
        })

@csrf_exempt
def add(request):
    title = "Main Window"
    artist = Artist()
    album = Album()
    song = Song()
    if request.method == 'POST':
        form = AddLyrics(request.POST)
        if form.is_valid():
            artistName = form.cleaned_data['artist']
            albumName = form.cleaned_data['album']
            songName = form.cleaned_data['song']
            song.lyrics = form.cleaned_data['lyrics']
            try:
                artist = Artist.objects.get(artist=artistName)
            except:
                artist.artist = artistName
                artist.save()
            try:
                album = Album.objects.get(album=albumName)
                print "AAAAAAAAA %s %s" % (albumName, album)
            except:
                album.album = albumName
                album.artist = artist
                album.save()
            try:
                song = Song.objects.get(song=songName)
                print "sadasdasds"
                render_to_response('song.html', {
                    "title": title,
                    "artist": song.artist,
                    "song" : song.song
                })
            except:
                print "ssaasa"
                song.song = songName
                song.artist = artist
                song.album = album
                song.save()

                return render_to_response('song.html', {
                    "title": title,
                    "artist":artist,
                    "song" : song
                })

    else:
        form = AddLyrics()
    return render_to_response('add.html', {
        'form': form,
        })

def search(request, letter):
    title = "Main Windfsdfsdsfow"
    artist = Artist.objects.filter(artist__startswith=letter)
    return render_to_response('search.html', {
        "title": title,
        "artist" : artist
    })

def artist(request, artist):

    artist = get_object_or_404(Artist, artist=artist)
    songs = Song.objects.filter(artist=artist)
    album = Album.objects.filter(artist=artist)
    title = "%s :: %s" % ( artist.artist, WEBSITE_NAME)

    return render_to_response('artist.html', {
        "title": title,
        "artist" : artist,
        "songs" : songs,
        "album" : album,
        })

def song(request, artist, album, song):

    artist = get_object_or_404(Artist, artist=artist)
    song = get_object_or_404(Song, song=song)
    title = "%s - %s :: %s" % ( artist.artist, song.song, WEBSITE_NAME)
    return render_to_response('song.html', {
        "title": title,
        "artist":artist,
        "song" : song
    })

@csrf_exempt
def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST': # If the form has been submitted...
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['me@5pd.ru']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
        })
