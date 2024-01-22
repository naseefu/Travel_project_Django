from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Tips(models.Model):
    image = models.ImageField(upload_to='pics')
    dates = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    caption = models.CharField(max_length=250)
    desc = models.TextField()

