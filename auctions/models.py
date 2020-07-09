from django.contrib.auth.models import AbstractUser
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.CharField(max_length=64)
    image_url = models.TextField()
    bid = models.IntegerField()
    active = models.BooleanField(default=True)
    owner = models.ManyToManyField('User')

    def __str__(self):
        return f"{self.title}"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, blank=True)
    

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="current_bid")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="bidder")
    price = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.listing} - ${self.price}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.user} - {self.listing}"
