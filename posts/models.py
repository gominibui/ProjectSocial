from django.db import models

from users.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False)

    def __str__(self):
        return self.title