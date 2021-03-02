from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
from meetings.models import Meeting


def welcome(request):
    """Welcome page for web app"""
    return render(
        request,
        'website/welcome.html',
        {"num_meetings": Meeting.objects.count()})


def date(request) -> HttpResponse:
    """"Return HTTP Response with the date"""
    return HttpResponse(f"This page was served at {dt.now()}")


def about(request) -> HttpResponse:
    """Section about us"""
    return HttpResponse("Cool python programmer building web app in django")
