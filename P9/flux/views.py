from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required
def home(request):
    return render(request, 'flux/home.html')


@login_required
def create_ticket(request):
    c_ticket_form = forms.TicketFormC()
    if request.method == 'POST':
        c_ticket_form = forms.TicketFormC(request.POST, request.FILES)
        print(request.FILES)
        if c_ticket_form.is_valid():
           c_ticket_form.save(commit=False)
           # ticket.author = request.user
           # ticket.save()
           return redirect('home')
    context = {
        'c_ticket_form': c_ticket_form,
            }
    return render(request, 'flux/ticket_create.html', context=context)


