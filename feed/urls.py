from django.conf.urls.defaults import *

urlpatterns = patterns('feed.views',
    url(r'^$', 'feed', name="feed_all"),
    url(r'^add/', 'add_feed', name="feed_add"),
)