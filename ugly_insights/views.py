from django.http import HttpResponse

def index(request):
    """
    Render the homepage of the site
    """

    return HttpResponse("Hello world!")
