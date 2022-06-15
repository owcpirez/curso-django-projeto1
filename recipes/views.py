from re import U

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')
    return render(request, 'recipes/home.html', context={
        'name': 'Oscar',
    })


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return render(request, 'temp.html')
