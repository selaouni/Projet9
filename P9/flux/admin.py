from django.contrib import admin
from flux.models import Ticket
from flux.models import UserFollows
from flux.models import Review


# Register your models here.

admin.site.register(Ticket)
admin.site.register(UserFollows)
admin.site.register(Review)