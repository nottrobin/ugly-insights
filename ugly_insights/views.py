import feedparser
import requests
from httpcache import CachingHTTPAdapter
from django_template_finder_view import TemplateFinder


class InsightsTemplateFinder(TemplateFinder):
    def get_context_data(self, **kwargs):
        """
        Add insights data to context
        """

        session = requests.Session()
        session.mount('http://', CachingHTTPAdapter())

        insights_feed = session.get('https://insights.ubuntu.com/feed')
        insights = feedparser.parse(insights_feed.text)

        context = {
            'title': insights.feed['title'],
            'posts': insights.entries
        }

        return context
