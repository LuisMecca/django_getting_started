from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt
from meetings.models import Meeting


def welcome(request):
    """Render a welcome view with a list of meetings scheduled"""
    return render(
        request,
        'website/welcome.html',
        {"meetings": Meeting.objects.all()}
    )


def date(request) -> HttpResponse:
    """"Render HTTP Response with the date"""
    return HttpResponse(f"This page was served at {dt.now()}")


def about(request) -> HttpResponse:
    """Render a section with information about us"""
    return HttpResponse("Cool python programmer building web app in django")
