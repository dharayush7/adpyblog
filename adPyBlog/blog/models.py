from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to="images")
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title+" - "+self.author
    

class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)



