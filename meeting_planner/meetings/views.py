from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Meeting, Room


def detail(request, id: int) -> HttpResponse:
    """ Render a detail information about a meeting
        based on the id of the meeting. If the id
        meeting do not exist get a 404 response
        -id: A int like::
        1
    """
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meeting/detail.html', {'meeting': meeting})


def rooms_list(request) -> HttpResponse:
    """ Render a list of rooms created for the meetings"""
    return render(
        request,
        'meeting/rooms_list.html',
        {'rooms': Room.objects.all()})
