from django.shortcuts import render

from .models import DoctorReg

def index(request):
    doctors = DoctorReg.objects.all()
    return render(request, 'index.html', {'doctorview': doctors})
# Create your views here.
