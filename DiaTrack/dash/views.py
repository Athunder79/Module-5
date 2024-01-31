from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def page2(request):
    return HttpResponse('<h1>Page 2</h1>')