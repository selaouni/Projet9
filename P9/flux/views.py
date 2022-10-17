from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.contrib import messages
from itertools import chain
from django.db.models import CharField, Value, Q
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy





# Create your views here.

@login_required
def home(request):

    review = models.Review.objects.all()
    review = review.annotate(content_type=Value("REVIEW", CharField()))
    # ticket = models.Ticket.objects.all()
    ticket = models.Ticket.objects.exclude(id__in=review.values("ticket_id"))
    ticket = ticket.annotate(content_type=Value("TICKET", CharField()))
    posts = sorted(chain(review, ticket), key=lambda post: (post.time_created), reverse=True)

    context = {"posts": posts}
    return render(request, 'flux/home.html', context=context)



@login_required
def create_ticket(request):
    c_ticket_form = forms.TicketFormC()
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES)
        # print(request.FILES)
        if c_ticket_form.is_valid():
           ticket = c_ticket_form.save(commit=False)
           ticket.user = request.user
           ticket.save()
           messages.success(request, "Ticket sauvegardé avec succes!")
           return redirect('home')
    context = {
        'c_ticket_form': c_ticket_form,
            }
    return render(request, 'flux/ticket_create.html', context=context)


@login_required
def create_review(request):
    c_ticket_form = forms.TicketFormC()
    c_review_form = forms.ReviewFormC()
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES)
        c_review_form = forms.ReviewFormC(request.POST)
        if all([c_ticket_form.is_valid(), c_review_form.is_valid()]):
           ticket = c_ticket_form.save(commit=False)
           ticket.user = request.user
           ticket.save()
           review = c_review_form.save(commit=False)
           review.user = request.user
           review.ticket = ticket
           review.save()
           messages.success(request, "Critique sauvegardée avec succes!")
           return redirect('home')
    context = {
        'c_ticket_form':c_ticket_form,
        'c_review_form': c_review_form,
            }
    return render(request, 'flux/review_create.html', context=context)

@login_required
def update_ticket(request,id):
    obj = models.Ticket.objects.get(id=id)
    c_ticket_form = forms.TicketFormC(instance=obj)
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES, instance=obj)
        if c_ticket_form.is_valid():
            ticket = c_ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Ticket modifié avec succes!")
            return redirect('home')
    context = {
        'c_ticket_form': c_ticket_form,
    }
    return render(request, 'flux/ticket_update.html', context=context)


@login_required
def delete_ticket(request, id):
    obj = models.Ticket.objects.get(id=id)
    c_ticket_form = forms.TicketFormC(instance=obj)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Ticket supprimé avec succes!")
        return redirect('post')
    context = {
        'c_ticket_form': c_ticket_form,
    }
    return render(request, 'flux/ticket_delete.html', context=context)

@login_required
def update_review(request,id):
    obj = models.Review.objects.get(id=id)
    # c_ticket_form = forms.TicketFormC(instance=obj)
    c_review_form = forms.ReviewFormC(instance=obj)
    if request.method == 'POST':
        # c_ticket_form = forms.TicketFormC(request.POST,request.FILES, instance=obj)
        c_review_form = forms.ReviewFormC(request.POST, instance=obj)
        # if all([c_ticket_form.is_valid(), c_review_form.is_valid()]):
        if c_review_form.is_valid():
            # ticket = c_ticket_form.save(commit=False)
            review = c_review_form.save(commit=False)
            review.user = request.user
            review.ticket = obj
            review.save()
            messages.success(request, "Critique modifiée avec succes!")
            return redirect('home')
    context = {
        "obj": obj,
        'c_review_form': c_review_form,
    }

    return render(request, 'flux/review_update.html', context=context)


@login_required
def delete_review(request, id):
    obj = models.Review.objects.get(id=id)
    c_ticket_form = forms.TicketFormC(instance=obj)
    c_review_form = forms.ReviewFormC(instance=obj)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Review supprimée avec succes!")
        return redirect('post')

    context = {
        'c_ticket_form': c_ticket_form,
        'c_review_form': c_review_form,
    }
    return render(request, 'flux/review_delete.html', context=context)

@login_required
def create_review_onticket(request,id):
    obj = models.Ticket.objects.get(id=id)
    c_review_form = forms.ReviewFormC()
    if request.method == 'POST':
        c_review_form = forms.ReviewFormC(request.POST)
        if c_review_form.is_valid():
            review = c_review_form.save(commit=False)
            review.user = request.user
            review.ticket = obj
            review.save()
            messages.success(request, "Critique sauvegardée avec succes!")
            return redirect('home')
    context = {
        "obj": obj,
        'c_review_form': c_review_form,
    }
    return render(request, 'flux/create_review_onticket.html', context=context)
@login_required
def post(request):
    review = models.Review.objects.select_related("ticket").filter(Q(user=request.user))
    review = review.annotate(content_type=Value("REVIEW", CharField()))
    ticket = models.Ticket.objects.filter(Q(user=request.user))
    ticket = ticket.annotate(content_type=Value("TICKET", CharField()))
    posts = sorted(chain(review, ticket), key=lambda post: (post.time_created), reverse=True)
    context = {"posts": posts}
    return render(request, "flux/post.html", context=context)

@login_required
def follow_users(request):
    follow_form = forms.FollowUsersForm()
    if request.method == 'POST':
        follow_form = forms.FollowUsersForm(request.POST)
        if follow_form.is_valid():
            form_follow = follow_form.save(commit=False)
            form_follow.user = request.user
            form_follow.save()

    following = models.UserFollows.objects.select_related("user").filter(Q(user=request.user))
    followed = models.UserFollows.objects.filter(followed_user=request.user)

    context = {
        "follow_form": follow_form,
        'following': following,
        'followed': followed,
    }
    return render(request, 'flux/subscription.html', context=context)



@login_required
def unsubscribe(request, id):
    obj = models.UserFollows.objects.get(id=id)
    follow_form = forms.FollowUsersForm(instance=obj)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Abonnement supprimée avec succes!")
        return redirect('subscription')

    context = {
        'follow_form': follow_form,

    }
    return render(request, 'flux/unsubscribe.html', context=context)



