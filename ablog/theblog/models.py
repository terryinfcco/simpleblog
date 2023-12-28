from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    # the on_delete will delete all the users blog posts if the user gets deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)