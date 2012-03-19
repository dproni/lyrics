from django.shortcuts import *
from main.models import Artist, Song, Album
from main.forms import *
from django.views.decorators.csrf import csrf_exempt
from haystack.views import SearchView

WEBSITE_NAME = "Lyricsy - the best place to share, translate, discover new lyrics on the web"

def main(request):
    title = "Lyrics"
    songs = Song.objects.order_by('rating')[:50]
    album = Album.objects.order_by('rating')[:7]
    artist = Artist.objects.order_by('rating')[:7]
    return render_to_response('main.html', {
        "title": title,
        "album": album,
        "songs": songs,
        "artist": artist,
        "main": True
    })


@csrf_exempt
def add(request):
    title = "Main Window"
    artist = Artist()
    album = Album()
    songG = Song()
    if request.method == 'POST':
        form = AddLyrics(request.POST)
        if form.is_valid():
            artistName = form.cleaned_data['artist']
            albumName = form.cleaned_data['album']

            albumPicture = form.cleaned_data['albumPicture']
            position = albumPicture.find('albums') - 1
            albumPicture = albumPicture[position:]
            print "albumPicture = %s" % (albumPicture)

            songName = form.cleaned_data['song']
            songG.lyrics = form.cleaned_data['lyrics']
            print "adding new song..."
            try:
                artist = Artist.objects.get(artist=artistName)
                print "artist %s already exist" % (artist)
            except:
                artist.artist = artistName
                artist.save()
                print "artist %s was added" % (artist)
            try:
                album = Album.objects.get(album=albumName)
                #renew album photo
                if albumPicture:
                    album.photo = albumPicture
                    album.save()
                    print "album picture renew " + albumPicture
                print "album %s is already exist" % (album)
            except:
                album.album = albumName
                album.artist = artist
                if albumPicture:
                    album.photo = albumPicture
                    print "album picture was added " + albumPicture
                album.save()
                print "album %s was added" % (album)

            # TODO: here you should implement logic for adding different translations for song
            #            try:
            #                song = Song.objects.get(song=songName)
            #                print "sadasdasds"
            #                render_to_response('song.html', {
            #                    "title": title,
            #                    "artist": song.artist,
            #                    "song" : song.song
            #                })
            #            except:

            songG.song = songName
            songG.artist = artist
            songG.album = album
            songG.save()
            print "song %s was added" % (songG)
            print "artist.id = %s, album.id = %s, song.id = %s" % (artist.id, album.id, songG.id)

            return song(request, artist.id, album.id, songG.id)

    else:
        form = AddLyrics()
    return render_to_response('add.html', {
        'form': form,
        })


def letter(request, letter):
    title = "Lyrics"
    artist = Artist.objects.filter(artist__startswith=letter)
    return render_to_response('letter.html', {
        "title": title,
        "artist": artist
    })


def number(request):
    title = "Lyrics"
    artist = Artist.objects.filter(artist__range=(0, 9))
    return render_to_response('letter.html', {
        "title": title,
        "artist": artist
    })


def artist(request, artist):
    artist = get_object_or_404(Artist, id=artist)
    album = Album.objects.filter(artist=artist)
    mainList = []

    for alb in album:
        albumSongs = Song.objects.filter(artist=artist, album=alb)
        albSongs = AlbumWithSongs(alb, albumSongs)
        mainList.append(albSongs)
    songs = Song.objects.filter(artist=artist)
    title = "%s :: %s" % ( artist.artist, WEBSITE_NAME)

    return render_to_response('artist.html', {
        "title": title,
        "artist": artist,
        "songs": songs,
        "mainList": mainList,
        })


def song(request, artist, song):
    artist = get_object_or_404(Artist, id=artist)
#    album = get_object_or_404(Album, id=album)
    song = get_object_or_404(Song, id=song)
    title = "%s - %s :: %s" % ( artist.artist, song.song, WEBSITE_NAME)
    return render_to_response('song.html', {
        "title": title,
        "artist": artist,
        "song": song,
        })


def album(request, artist, album):
    artist = get_object_or_404(Artist, id=artist)
    album = get_object_or_404(Album, id=album)
    song = Song.objects.filter(artist=artist, album=album)
    title = "%s :: %s" % ( album.album, WEBSITE_NAME)
    return render_to_response('album.html', {
        "title": title,
        "album": album,
        "artist": artist,
        "song": song
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


def ajax_lyrics(request, artist, album, song):
    artist = get_object_or_404(Artist, id=artist)
    song = get_object_or_404(Song, id=song)
    title = "%s - %s :: %s" % ( artist.artist, song.song, WEBSITE_NAME)
    return render_to_response('ajax_song.html', {
        "title": title,
        "artist": artist,
        "song": song
    })


def ajax_song_info(request, artist, album, song):
    artist = get_object_or_404(Artist, id=artist)
    song = get_object_or_404(Song, id=song)
    songListAll = Song.objects.filter(artist=artist)
    title = "%s - %s :: %s" % ( artist.artist, song.song, WEBSITE_NAME)
    return render_to_response('ajax/ajax_song_info.html', {
        "title": title,
        "artist": artist,
        "song": song,
        "songListAll": songListAll,
        })

#this class is used to show list of albums with their songs in artist.html
class AlbumWithSongs:
    album = 0
    songList = []

    def __init__(self, album, songList):
        self.album = album
        self.songList = songList


class SimpleSearchView(SearchView):
    def __name__(self):
        return "SimpleSearchView"

    def extra_context(self):
        extra = super(SimpleSearchView, self).extra_context()
        return extra

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        (paginator, page) = self.build_page()
        print "view"

        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'paginator': paginator,
            'suggestion': None,
            }

        if getattr(settings, 'HAYSTACK_INCLUDE_SPELLING', False):
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())
        return "ff"
