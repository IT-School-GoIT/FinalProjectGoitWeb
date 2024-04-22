from django.shortcuts import render



def index(request):
    return render(request, 'news/index.html', {
        'title': 'Новини',
        'page': 'index',
        'app': 'news'
    })

# def news(request):
#     return render(request, 'news/news.html', {
#         'title': 'Новини',
#         'page': 'news',
#         'app': 'news'
#     })