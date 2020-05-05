from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html', {'hi': 'thi is me'})


def sushi(request):
    return HttpResponse('Sushi is amazing!')
