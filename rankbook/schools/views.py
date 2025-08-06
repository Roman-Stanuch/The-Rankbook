from django.shortcuts import render

# Create your views here.

from .models import School

def index(request):
    return render(request, "schools/index.html", {
        "schools": School.objects.all()
    })

def school_home(request, school):
    school_data = School.objects.filter(name=school).first()
    rankings = []
    if len(school_data.rankings.all()) > 0:
        rankings = school_data.rankings.all()

    return render(request, "schools/school_home.html", {
        "school": school,
        "rankings": rankings
    })