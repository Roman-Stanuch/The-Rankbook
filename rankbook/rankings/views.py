from django.shortcuts import render

import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    rankings = ["Cornell", "Madison", "Carnegie"]
    return render(request, "rankings/index.html", {
        "date": now.date(),
        "rankings": rankings
    }) 

def submit(request):
    return render(request, "rankings/submit.html")