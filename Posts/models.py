from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    is_for_sale = models.BooleanField(default=False)

    rooms = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    city = models.CharField(max_length=120)

    address = models.CharField(max_length=200)
    description = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    image_1 = models.ImageField(upload_to='images/', blank=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
