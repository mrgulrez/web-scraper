# from django.db import models

# # Create your models here.
# class ScrapedData(models.Model):
#     data = models.TextField()

#     def __str__(self):
#         return self.data[:50]

from django.db import models

class ExtractedData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

