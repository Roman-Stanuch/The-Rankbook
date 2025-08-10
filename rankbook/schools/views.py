from django.shortcuts import render

# Create your views here.

from .models import School

def index(request):
    return render(request, "schools/index.html", {
        "schools": School.objects.all()
    })

def school_home(request, school_id):
    school_data = School.objects.get(pk=school_id)
    rankings = school_data.rankings.all()

    return render(request, "schools/school_home.html", {
        "school_data": school_data,
        "rankings": rankings
    })