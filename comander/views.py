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

@login_required
def deleted_done(request):
    return render(request, 'comander/delete.html', {
        'title': 'deleted_done',
        'page': 'deleted_done',
        'app': 'comander'
    })


@login_required
def change_done(request):
    return render(request, 'comander/change_done.html', {
        'title': 'change_done',
        'page': 'change_done',
        'app': 'comander'
    })

@login_required
def add_note(request):
    return render(request, 'comander/add_note.html', {
        'title': 'add_note',
        'page': 'add_note',
        'app': 'comander'
    })

@login_required
def all_notes(request):
    return render(request, 'comander/all_notes.html', {
        'title': 'all_notes',
        'page': 'all_notes',
        'app': 'comander'
    })


@login_required
def change_note(request):
    return render(request, 'comander/change_note.html', {
        'title': 'change_note',
        'page': 'change_note',
        'app': 'comander'
    })


@login_required
def change_note_done(request):
    return render(request, 'comander/change_note_done.html', {
        'title': 'change_note_done',
        'page': 'change_note_done',
        'app': 'comander'
    })