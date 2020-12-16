from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    task_id = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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
