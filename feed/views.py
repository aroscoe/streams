from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.utils import simplejson as json

from feed.models import Feed
from feed.forms import FeedForm
from feed.utils.aggregator import get_stream

def feed(request):
    feed = Feed.objects.get(pk=1)
    streams = get_stream(feed.url)
    return direct_to_template(request, 'feed/base.html', locals())

def add_feed(request):
    if request.method == 'POST':
        feed_form = FeedForm(request.POST)
        
        if feed_form.is_valid():
            feed_form.save() # TODO: add listener to update live streams when a new feed is added
            response = {'status': 1}
        else:
            response = {'status': 0}
        
        return HttpResponse(json.dumps(response), mimetype='application/json')
    else:
        raise Http404
    