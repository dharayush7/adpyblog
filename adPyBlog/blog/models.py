from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type=models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug=models.SlugField(max_length=250)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title+" - "+self.author


