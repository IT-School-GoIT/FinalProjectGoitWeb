from django.shortcuts import render

def index(request):
    return render(request, 'comander/index.html', {
        'title': 'Команди',
        'page': 'index',
        'app': 'comander'
    })