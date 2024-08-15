from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

