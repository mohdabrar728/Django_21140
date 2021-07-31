from django.shortcuts import render


# Create your views here.
def show(request):
    var = request.session.get('count', 0)
    counter = var + 1
    request.session['count'] = counter
    return render(request, 'base.html', {'counter': counter, 'refresh': 'refresh',
                                         'start': 'btn-light', 'stop': 'btn-outline-light'})


def stop(request):
    if 'count' in request.session:
        del request.session['count']
    return render(request, 'base.html', {'counter': 0, 'refresh': '',
                                         'stop': 'btn-light', 'start': 'btn-outline-light'})
