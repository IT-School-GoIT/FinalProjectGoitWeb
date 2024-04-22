from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View


@login_required
def index(request):
    return render(request, 'comander/index.html', {
        'title': 'Commands',
        'page': 'index',
        'app': 'comander'
    })


@login_required
def add(request):
    return render(request, 'comander/add.html', {
        'title': 'add',
        'page': 'add',
        'app': 'comander'
    })


@login_required
def search_all(request):
    return render(request, 'comander/search_all.html', {
        'title': 'search_all',
        'page': 'search_all',
        'app': 'comander'
    })



@login_required
def change(request):
    return render(request, 'comander/change.html', {
        'title': 'change',
        'page': 'change',
        'app': 'comander'
    })


@login_required
def delete(request):
    return render(request, 'comander/delete.html', {
        'title': 'delete',
        'page': 'delete',
        'app': 'comander'
    })


@login_required
def sorting_files(request):
    return render(request, 'comander/sorting_files.html', {
        'title': 'sorting_files',
        'page': 'sorting_files',
        'app': 'comander'
    })


@login_required
def birhday_contact(request):
    return render(request, 'comander/birhday_contact.html', {
        'title': 'birhday_contact',
        'page': 'birhday_contact',
        'app': 'comander'
    })

@login_required
def download(request):
    return render(request, 'comander/download.html', {
        'title': 'download',
        'page': 'download',
        'app': 'comander'
    })


@login_required
def view_file(request):
    return render(request, 'comander/view_file.html', {
        'title': 'view_file',
        'page': 'view_file',
        'app': 'comander'
    })



@login_required
def contact_card(request):
    return render(request, 'comander/contact_card.html', {
        'title': 'contact_card',
        'page': 'contact_card',
        'app': 'comander'
    })