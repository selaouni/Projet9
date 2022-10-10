from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.contrib import messages


# Create your views here.

@login_required
def home(request):
#code pour flux
    flux = models.Ticket.objects.all()
    return render(request, 'flux/home.html', context={'flux': flux})
#   return render(request, 'flux/home.html')


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
           review.save()
           messages.success(request, "Critique sauvegardée avec succes!")
           return redirect('home')
    context = {
        'c_review_form': c_review_form,
            }
    return render(request, 'flux/review_create1.html', context=context)


@login_required
def subscription_page(request):
    return render(request, 'flux/subscription.html')

# @login_required
# def create_ticket(request):
#     c_ticket_form = forms.TicketFormC()
#     if request.method == 'POST':
#         c_ticket_form = forms.TicketFormC(request.POST)
#         print(request.FILES)
#         if c_ticket_form.is_valid():
#            ticket = c_ticket_form.save(commit=False)
#            ticket.author = request.user
#            # c_ticket_form.cleaned_data["user"] = request.user
#            ticket.save()
#
#
#            messages.success(request, "Ticket sauveagradé avec success!")
#         return redirect('home')
#     context = {
#         'c_ticket_form': c_ticket_form,
#             }
#     return render(request, 'flux/ticket_create.html', context=context)
