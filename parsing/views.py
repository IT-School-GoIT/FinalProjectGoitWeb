from django.shortcuts import render
from django.shortcuts import redirect

from .models import News
from .news import save_news_to_database, politika_news, other_news, auto_news, health_news, economy_news, clear_database, sport_news, tourism_news, science_and_it_news


def list_news(request):
    other = News.objects.filter(category='Other')
    politika = News.objects.filter(category='Politika')
    cars = News.objects.filter(category='Cars')
    health = News.objects.filter(category='Health')
    economy = News.objects.filter(category='Economy')
    sport = News.objects.filter(category='Sport')
    tourism = News.objects.filter(category='Tourism')
    science = News.objects.filter(category='Science')
    # return render(request, '_fragments/news.html', {
    return render(request, 'home/news.html', {
        'other': other,
        'politika': politika,
        'cars': cars,
        'health': health,
        'economy': economy,
        'sport': sport,
        'tourism': tourism,
        'science': science,
    })


def add_news(request):
    clear_database()
    context = other_news('https://tsn.ua/other')
    politika = politika_news('https://tsn.ua/politika')
    cars = auto_news('https://tsn.ua/auto')
    health = health_news('https://tsn.ua/zdorovya')
    economy = economy_news('https://tsn.ua/groshi')
    sport = sport_news('https://tsn.ua/prosport')
    tourism = tourism_news('https://tsn.ua/tourism')
    science = science_and_it_news('https://tsn.ua/nauka_it')
    save_news_to_database(context)
    save_news_to_database(politika)
    save_news_to_database(cars)
    save_news_to_database(health)
    save_news_to_database(economy)
    save_news_to_database(sport)
    save_news_to_database(tourism)
    save_news_to_database(science)
    return redirect('news')


