from django.shortcuts import render
import pygame

# Create your views here.
def show(request):
    var = request.session.get('count', 0)
    counter = var + 1
    request.session['count'] = counter
    return render(request, 'base.html', {'counter': counter, 'refresh': 'refresh',
                                         'start': 'btn-light', 'pause': 'btn-outline-light',
                                         'stop': 'btn-outline-light'})


def stop(request):
    if 'count' in request.session:
        del request.session['count']
    return render(request, 'base.html', {'counter': 0, 'refresh': '',
                                         'stop': 'btn-light', 'pause': 'btn-outline-light',
                                         'start': 'btn-outline-light'})


def pause(request):
    var1 = request.session.get('count')
    return render(request, 'base.html', {'counter': var1, 'refresh': '',
                                         'stop': 'btn-outline-light', 'pause': 'btn-light',
                                         'start': 'btn-outline-light'})
