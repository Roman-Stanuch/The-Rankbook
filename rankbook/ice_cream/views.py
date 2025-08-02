from django.shortcuts import render

import datetime

# Create your views here.
def index(request):
    return render(request, "ice_cream/index.html") 

def named_request(request, name):
    now = datetime.datetime.now()
    return render(request, "ice_cream/named_request.html", {
        "name": name.capitalize(),
        "date": now.date()
    }) 