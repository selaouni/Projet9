from django.forms import ModelForm
from django.db import models
from . import models
from django import forms
from django.conf import settings


class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
    image = forms.ImageField(label_suffix="", required=False)


class ReviewForm(ModelForm):
    RATINGS_CHOICES = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
    rating = forms.ChoiceField(label="Note", widget=forms.RadioSelect, choices=RATINGS_CHOICES)




class FollowUsersForm(ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']



# class FollowedDeleteForm(ModelForm):
#     class Meta:
#         model = models.UserFollows
#         fields = ['followed_user']
