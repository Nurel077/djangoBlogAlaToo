from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120,blank=True,null=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.FloatField
    legals = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title