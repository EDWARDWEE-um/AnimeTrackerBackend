from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField( max_length=250 )
    type = models.CharField(max_length=250)
    episodes = models.IntegerField(default=0)
    image_url = models.TextField(default="")
    url = models.TextField(default="")
    synopsis = models.TextField(default="")
    score = models.FloatField(default=0)
    published = models.DateTimeField(default=timezone.now)
    author = models.EmailField()
    class Meta:
        unique_together = ["title", "author"]

    def __str__(self):
        return self.title
    
