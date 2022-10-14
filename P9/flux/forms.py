from django.forms import ModelForm
from django.db import models
from . import models
from django import forms
from django.conf import settings


class TicketFormC(ModelForm):
    class Meta:
        model = models.Ticket
        # titre = forms.TextInput()
        # description = forms.TextInput()
        fields = ['title', 'description', 'image']
    # title = forms.CharField(label="Titre", label_suffix="")
    # description = forms.CharField(max_length=2048, label_suffix="")
    image = forms.ImageField(label_suffix="", required=False)


class ReviewFormC(ModelForm):
    RATINGS_CHOICES = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
    # title = forms.CharField(label="Titre", label_suffix="")
    # Description = forms.CharField(max_length=2048, label_suffix="")
    # image = forms.ImageField(label_suffix="", required=False, )
    # headline = forms.CharField(max_length=128, label="Titre")
    rating = forms.ChoiceField(label="Note", widget=forms.RadioSelect, choices=RATINGS_CHOICES)
    # body = forms.CharField(max_length=8192, label="Commentaire")



class FollowUsersForm(ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']



# class FollowedDeleteForm(ModelForm):
#     class Meta:
#         model = models.UserFollows
#         fields = ['followed_user']
