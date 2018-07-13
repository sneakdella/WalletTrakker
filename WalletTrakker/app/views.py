"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

## CUSTOM IMPORTS
import googlemaps
from app.scrape import *

def home(request):
    """Renders the home page."""
    test = "lol"
    information = update_map()
    dev_id = information[0]
    lat = information[1]
    long = information[2]
    print("MAP FUNCTION: " + str(update_map()))

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Tracking Page',
            'year':datetime.now().year,
            'test': test,
            'lat': lat,
            'long': long,
            'dev_id': dev_id,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
