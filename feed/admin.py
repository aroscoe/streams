from django.contrib import admin

from feed.models import *

admin.site.register(Feed)
admin.site.register(FeedItem)