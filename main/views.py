from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from main.forms import *


def info(request):
    title = "Main Window"
    lyrics = Lyrics.objects.get(id=1)
    return render_to_response('info.html', {
            "title": title,
            "lyrics" : lyrics
            })

@csrf_exempt
def add(request):
    title = "Main Window"
    lyrics = Lyrics()
    if request.method == 'POST':
        form = AddLyrics(request.POST)
        if form.is_valid():
            lyrics.artist = form.cleaned_data['artist']
            lyrics.song = form.cleaned_data['song']
            lyrics.lyrics = form.cleaned_data['lyrics']
            lyrics.save()
            return render_to_response('info.html', {
            "title": title,
            "lyrics" : lyrics
            })
    else:
        form = AddLyrics()
    return render_to_response('add.html', {
        'form': form,
    })

def addLyrics():
    lyrics = Lyrics()
    lyrics.artist = "RIHANNA"
    lyrics.song = "S&M"
    lyrics.lyrics = '''
        Na na na
Come on
Na na na
Come on
Na na na na na
Come on
Na na na
Come on
Come on
Come on
Na na na na
Come on
Na na na
Come on
Na na na na na
Come on
Na na na
Come on
Come on
Come on
Na na na na

Feels so good being bad
There's no way I'm turning back
Now the pain is my pleasure
Cause nothing could measure

Love is great, love is fine
Out the box, out of line
The affliction of the feeling
Leaves me wanting more

[Chorus x2:]
Cause I may be bad
But I'm perfectly good at it
Sex in the air
I don't care
I love the smell of it
Sticks and stones
May break my bones
But chains and whips
Excite me

Na na na na
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it

Love is great, love is fine
Out the box, out of line
The affliction of the feeling
Leaves me wanting more

[Chorus:]
Cause I may be bad
But I'm perfectly good at it
Sex in the air
I don't care
I love the smell of it
Sticks and stones
May break my bones
But chains and whips
Excite me

Na na na na
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it

S...S...S
And
M...M...M
S...S...S
And
M...M...M

Oh
I love the feeling
You bring to me
Oh, you turn me on
It's exactly what
I've been yearning for
Give it to me strong

And meet me in my boudoir
Make my body say ah, ah, ah

I like it
Like it

[Chorus x2:]
Cause I may be bad
But I'm perfectly good at it
Sex in the air
I don't care
I love the smell of it
Sticks and stones
May break my bones
But chains and whips
Excite me

Na na na na
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it
Come on
Come on
Come on
I like it
Like it

S...S...S
And
M...M...M
S...S...S
And
M...M...M
S...S...S
And
M...M...M
S...S...S
And
M...M...M'''
    lyrics.save()