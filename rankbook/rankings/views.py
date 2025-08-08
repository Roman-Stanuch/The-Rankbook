from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ranking
from schools.models import School

import datetime

class NewVoteForm(forms.Form):
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label="Select a School")
    business = forms.CharField(label="Business")
    type = forms.CharField(label="Type")

# Create your views here.
def index(request):
    return render(request, "rankings/index.html", {
        "rankings": Ranking.objects.all() 
    }) 

def submit(request):
    if request.method == "POST":
        form = NewVoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            entered_school = data["school"]
            entered_business = data["business"]
            entered_type = data["type"]

            ranking, created = Ranking.objects.update_or_create(school=entered_school, business=entered_business, type=entered_type)
            ranking.votes += 1
            ranking.save()

            return HttpResponseRedirect(reverse("rankings:index"))
        else:
            return render(request, "rankings/submit.html", {
                "form": form 
            })

    return render(request, "rankings/submit.html", {
        "form": NewVoteForm()
    })