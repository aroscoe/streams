#!/usr/bin/env python

from feed.models import *

import feedparser

def get_stream(url):
    parsed_feed = feedparser.parse(url)
    stream = []
    for entry in parsed_feed.entries:
        data = {
            "title": entry.title,
            "link": entry.link,
            "summary": entry.get("summary")
        }
        stream.append(data)
    return stream