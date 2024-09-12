from django.shortcuts import render
from .models import Settings, Team

def index(request):
    settings = Settings.objects.latest('id')
    students = Team.objects.all()
    return render(request, 'index.html', locals())


# Create your views here.
