from django.shortcuts import render
from .forms import Form

def index(request):
    if request.method == 'POST':
        print(dir(request.POST))
        return render(request, 'index.html', context={'data': str(list(request.POST.items()))})
    return render(request, 'index.html')


def form(req):
    return render(req, 'form.html', context={'form': Form})


def order(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render(request, 'order.html', context={
                'form': form,
                'data': request.POST
            })
    else:
        form = Form()

    return render(request, 'order.html', {'form': form})
