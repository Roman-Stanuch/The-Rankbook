from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Ranking, RankingCategory
from schools.models import School

import datetime

class NewVoteForm(forms.Form):
    category = forms.ModelChoiceField(queryset=RankingCategory.objects.all(), empty_label="Select a Category")
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label="Select a School")
    business = forms.CharField(label="Business or Object Name")

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
            submitted_category = data["category"]
            submitted_school = data["school"]
            submitted_business = data["business"]

            ranking, created = Ranking.objects.update_or_create(category=submitted_category, school=submitted_school, business=submitted_business)
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