from django import forms

class AddLyrics(forms.Form):
    artist      = forms.CharField(max_length=10)
    song        = forms.CharField(max_length=100)
    album       = forms.CharField(max_length=100, required=False)
    lyrics      = forms.CharField(widget=forms.widgets.Textarea())


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)