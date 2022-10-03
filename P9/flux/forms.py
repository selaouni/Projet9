from django.forms import ModelForm
from django.db import models
from . import models
from django import forms


class TicketFormC(ModelForm):
    class Meta:
        model = models.Ticket
        # titre = forms.TextInput()
        # description = forms.TextInput()
        fields = ['title', 'description', 'image']
    title = forms.CharField(label="Titre", label_suffix="")
    description = forms.CharField(max_length=2048, label_suffix="")
    image = forms.ImageField(label_suffix="", required=False, )


class ReviewFormC(forms.Form):
    class Meta:
        model = models.Review
        # titre = forms.TextInput()
        # description = forms.TextInput()
        fields = ['title', 'description']

