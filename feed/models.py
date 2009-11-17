from django.db import models

class Feed(models.Model):
    name     = models.CharField(max_length=125)
    url      = models.URLField()
    modified = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    class Admin:
        pass

class FeedItem(models.Model):
    title   = models.CharField(max_length=150)
    summary = models.TextField()
    url     = models.URLField(verify_exists=False, blank=True)
    read    = models.DateField()
    feed    = models.ForeignKey(Feed)
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass
