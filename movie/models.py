from django.db import models
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)


class Review(models.Model):
    title_review = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text_review = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    image_review = models.ImageField(upload_to= 'movie/images/')    #La subo en la misma carpeta solo por practicidad para este ejericio