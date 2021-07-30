from django.shortcuts import render


# Create your views here.
def show(request):
    var = request.session.get('count', 0)
    counter = var + 1
    request.session['count'] = counter
    return render(request, 'base.html', {'counter': counter})
