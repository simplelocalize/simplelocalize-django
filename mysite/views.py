from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_language

def hello_world(request):
    activate('es')
    print(f"Current language: {get_language()}")
    
    # Translators: This message appears on the home page only
    output = _("Welcome to my site.")
    print(f"Translation: {output}")
    return HttpResponse(output)