from django.db import models
from django.db.models.signals import post_save


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    task_id = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


def save_keyword(sender, instance, **kwargs):
    print("Received the signal")

post_save.connect(save_keyword, sender=Keyword)


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    published_at = models.DateTimeField()
    thumnail_url = models.URLField() 
    keyword = models.ManyToManyField(Keyword, related_name='videos')

    def __str__(self):
        return self.title
