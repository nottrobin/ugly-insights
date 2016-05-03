from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Render the homepage of the site
    """

    context = {'temporary_content': 'Hello world!'}

    return render(request, 'index.html', context)
