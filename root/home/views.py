from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home'
    })

def about(request):
    return render(request, 'home/about.html', {
        'title': 'Про сайт',
        'page': 'about',
        'app': 'home'
    })

def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home'
    })
