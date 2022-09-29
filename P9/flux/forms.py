from django.forms import ModelForm
from django import forms
from . import models


class TicketFormC(forms.Form):
    class Meta:
        model = models.Ticket()
        titre = forms.TextInput()
        description = forms.TextInput()
        fields = ['title', 'description']


