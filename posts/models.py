from django.db import models

# Create your models here.

class Posts(models.Model):


    title = models.CharField(max_length=255)
    content = models.TextField()
    if_featured = models.BooleanField(default = False)

    def __str__(self):

        return self.title
