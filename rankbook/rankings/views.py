from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import datetime

class NewVoteForm(forms.Form):
    school = forms.CharField(label="School")
    business = forms.CharField(label="Business")
    type = forms.CharField(label="Type")

# Create your views here.
def index(request):
    if "rankings" not in request.session:
        request.session["rankings"] = []

    return render(request, "rankings/index.html", {
        "rankings": request.session["rankings"] 
    }) 

def submit(request):
    if request.method == "POST":
        form = NewVoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            school = data["school"]
            business = data["business"]
            type = data["type"]
            request.session["rankings"] += [school + " with " + type + " from " + business]
            return HttpResponseRedirect(reverse("rankings:index"))
        else:
            return render(request, "rankings/submit.html", {
                "form": form 
            })

    return render(request, "rankings/submit.html", {
        "form": NewVoteForm()
    })