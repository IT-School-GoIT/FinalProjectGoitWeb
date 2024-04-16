from django.shortcuts import render
from django.views import View

def index(request):
    return render(request, 'comander/index.html', {
        'title': 'Commands',
        'page': 'index',
        'app': 'comander'
    })

def add(request):
    return render(request, 'comander/add.html', {
        'title': 'add',
        'page': 'add',
        'app': 'comander'
    })

def search_all(request):
    return render(request, 'comander/search_all.html', {
        'title': 'search_all',
        'page': 'search_all',
        'app': 'comander'
    })


def change(request):
    return render(request, 'comander/change.html', {
        'title': 'change',
        'page': 'change',
        'app': 'comander'
    })

def delete(request):
    return render(request, 'comander/delete.html', {
        'title': 'delete',
        'page': 'delete',
        'app': 'comander'
    })


def sorting_files(request):
    return render(request, 'comander/sorting_files.html', {
        'title': 'sorting_files',
        'page': 'sorting_files',
        'app': 'comander'
    })

def birhday_contact(request):
    return render(request, 'comander/birhday_contact.html', {
        'title': 'birhday_contact',
        'page': 'birhday_contact',
        'app': 'comander'
    })