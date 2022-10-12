from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.contrib import messages
from itertools import chain
from django.db.models import CharField, Value, Q



# Create your views here.

@login_required
def home(request):

    flux_ticket = models.Ticket.objects.all()
    # flux_review = models.Review.object.all()
    context = {
        'flux_ticket': flux_ticket,
        # 'flux_review': flux_review,
            }
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
def follow_users(request):
    follow_form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        follow_form = forms.FollowUsersForm(request.POST, instance=request.user)
        if follow_form.is_valid():
            user_follow_form = follow_form.save()
            # user_follow_form.follows.add(id)
            return redirect('home')
    return render(request, 'flux/subscription.html')



@login_required
def post(request):
    review = models.Review.objects.select_related("ticket").filter(Q(user=request.user))
    review = review.annotate(content_type=Value("REVIEW", CharField()))
    ticket = models.Ticket.objects.filter(Q(user=request.user)).exclude(id__in=review.values("ticket_id"))
    ticket = ticket.annotate(content_type=Value("TICKET", CharField()))
    posts = sorted(chain(review, ticket), key=lambda post: (post.time_created), reverse=True)
    context = {"posts": posts}
    return render(request, "flux/post.html", context=context)

@login_required
def update_ticket(request):
    obj = models.Ticket.objects.get(id=25)
    c_ticket_form = forms.TicketFormC()
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES, instance=obj)
        # print(request.FILES)
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
def delete_ticket(request):
    return render(request, 'flux/ticket_delete.html')

@login_required
def update_review(request):
    obj = models.Ticket.objects.get(id=25)
    c_ticket_form = forms.TicketFormC()
    c_review_form = forms.ReviewFormC()
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES, instance=obj)
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
        'c_ticket_form': c_ticket_form,
        'c_review_form': c_review_form,
    }

    return render(request, 'flux/review_update.html', context=context)

@login_required
def delete_review(request):
    return render(request, 'flux/review_delete.html')


