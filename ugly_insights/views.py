import feedparser
import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Render the homepage of the site
    """

    insights_feed = requests.get('https://insights.ubuntu.com/feed')
    insights = feedparser.parse(insights_feed.text)

    context = {
        'title': insights.feed['title'],
        'posts': insights.entries
    }

    return render(request, 'index.html', context)
