from django.shortcuts import render
from django.http import HttpResponse


insulin = [
    {
        'dose': '5',
        'type': 'Fast-Acting',
        'note': 'This is a note.',
        'date_administered': '12/07/2023',
        'time_administered': '12:00'
    },

    {
        'dose': '5.5',
        'type': 'Nighttime',
        'note': 'This is a note.',
        'date_administered': '12/07/2023',
        'time_administered': '21:00'
    },

]


def home(request):
    context = {
        'insulin': insulin
    }
    return render(request, 'dash/home.html', context)

def detail(request):
    return HttpResponse('<h1>detail</h1>')
