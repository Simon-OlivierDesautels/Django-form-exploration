from django.db import models

class Review(models.Model):
    full_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField()
    # owner_comment = models.TextField()