from django.shortcuts import render

def index(request):
    return render(request, 'team/index.html', {
        'title': 'Команда',
        'page': 'index',
        'app': 'team'
    })