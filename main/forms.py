from django import forms
from haystack.forms import SearchForm
import os

def fix_os_paths(x):
    if isinstance(x, basestring):
        return x.replace('\\', '/')
    elif isinstance(x, tuple):
        return tuple(fix_os_paths(list(x)))
    elif isinstance(x, list):
        return [fix_os_paths(y) for y in x]
    else:
        return x


class AddLyrics(forms.Form):
    POSSIBLE_COUNTRIES = (
        ('Ru', 'Russian'),
        ('En', 'Engleesh'),
        ('Ge', 'Germany'),
        ('Fr', 'French'),
        ('Sp', 'Spanish')
        )
    TEXT_TYPES = (
        ('lyric', 'Lyric'),
        ('tab', 'Tab'),
        ('chord', 'Chord'),
        ('translation', 'Translation')
        )
    artist = forms.CharField(max_length=100)
    song = forms.CharField(max_length=100)
    album = forms.CharField(max_length=100, required=False)

    # create path to directory /albums
    path = __file__
    path = os.path.dirname(path) + '/'
    fix_os_paths(path)
    path = path[:-5] + 'albums'
    print "path = %s" % (path)

    albumPicture = forms.FilePathField(path=path, match='.jpg$')
    albumPicture.choices.sort()
    lang = forms.ChoiceField(choices=POSSIBLE_COUNTRIES)
    textType = forms.ChoiceField(choices=TEXT_TYPES)
    lyrics = forms.CharField(widget=forms.widgets.Textarea())


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class SimpleSearchForm(SearchForm):
#    start_date = forms.DateField(required=False)
#    end_date = forms.DateField(required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(SimpleSearchForm, self).search()

        return sqs