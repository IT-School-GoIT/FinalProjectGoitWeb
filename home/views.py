from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(
        request, "home/index.html", {"title": "Головна", "page": "index", "app": "home"}
    )


def about(request):
    return render(
        request,
        "home/about.html",
        {"title": "Про сайт", "page": "about", "app": "home"},
    )


def contacts(request):
    return render(
        request,
        "home/contacts.html",
        {"title": "Контакти", "page": "contacts", "app": "home"},
    )


def news(request):
    return render(
        request, "home/news.html", {"title": "Новини", "page": "news", "app": "home"}
    )


def project_topic(request):
    return render(
        request,
        "home/project_topic.html",
        {"title": "Тема проєкту", "page": "project_topic", "app": "home"},
    )


def exchange_rate(request):
    return render(
        request,
        "home/exchange_rate.html",
        {"title": "Курс валют", "page": "exchange_rate", "app": "home"},
    )


def privacy_policy(request):
    return render(
        request,
        "home/privacy_policy.html",
        {"title": "Політика конфіденційності", "page": "privacy_policy", "app": "home"},
    )

def presentation_of_the_project(request):
    return render(
        request,
        "home/presentation_of_the_project.html",
        {"title": "Презентація проєкту Fox.Web.", "page": "presentation_of_the_project", "app": "home"},
    )
