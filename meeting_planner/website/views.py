from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt


def welcome(request):
    """Welcome page for web app"""
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request) -> HttpResponse:
    """"Return HTTP Response with the date"""
    return HttpResponse(f"This page was served at {dt.now()}")


def about(request) -> HttpResponse:
    """Section about us"""
    return HttpResponse("Cool python programmer building web app in django")
