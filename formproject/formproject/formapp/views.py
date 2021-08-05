from django.shortcuts import render

# Create your views here.
from .forms import StuForms


def index(request):
    form = StuForms()
    return render(request, 'index.html', {'form1': form})

def posting(request):
    if request.method == 'POST':
        print(request.method)
        form = StuForms(request.POST)
        if form.is_valid():
            a = form.cleaned_data['name']
            b = form.cleaned_data['email']
            c = form.cleaned_data['passwd']
        return render(request, 'post.html', {'name':a,'email': b, 'pass': c})
    # else:
    #     form = StuForms()
    #     return render(request, 'index.html')
