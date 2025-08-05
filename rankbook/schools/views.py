from django.shortcuts import render

# Create your views here.

def index(request):
    if "schools" not in request.session:
        request.session["schools"] = ["Purdue"]

    return render(request, "schools/index.html", {
        "schools": request.session["schools"]
    })

def school_home(request, school):
    return render(request, "schools/school_home.html", {
        "school": school
    })