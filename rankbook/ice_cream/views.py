from django.shortcuts import render

import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    rankings = ["Cornell", "Madison", "Carnegie"]
    return render(request, "ice_cream/index.html", {
        "date": now.date(),
        "rankings": rankings
    }) 

def submit(request):
    return render(request, "ice_cream/submit.html")