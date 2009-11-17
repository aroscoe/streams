from django.forms import ModelForm

from feed.models import Feed

class FeedForm(ModelForm):
    class Meta:
        model = Feed