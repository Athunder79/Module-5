from django.shortcuts import render
from django.http import HttpResponse
from .models import Insulin



def home(request):
    context = {
        'insulin': Insulin.objects.all()
    }   
    return render(request, 'dash/home.html', context)

def detail(request):
    return HttpResponse('<h1>detail</h1>')
