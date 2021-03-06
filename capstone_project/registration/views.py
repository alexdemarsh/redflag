from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def login(request):
	return HttpResponse("login request")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/repository/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })