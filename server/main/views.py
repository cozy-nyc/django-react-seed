import os
from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render

def index(request):
    """This is the view for the home page

    Note:
        The context in home needs to be made global
    """
    context = {
    }
    template = 'index.html'
    return render(request, template, context)
