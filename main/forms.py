from django import forms

class AddLyrics(forms.Form):
    artist      = forms.CharField(max_length=10)
    song        = forms.CharField(max_length=100)
    lyrics      = forms.CharField(widget=forms.widgets.Textarea())
