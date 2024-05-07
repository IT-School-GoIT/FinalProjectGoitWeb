from django.db import models


# Create your models here.
class News(models.Model):
    category = models.CharField(max_length=100)
    short_description = models.TextField()
    news_link = models.URLField()
    photo_link = models.URLField()

    def __str__(self):
        return self.short_description
