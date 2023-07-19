from django.db import models

# Create your models here.
class Resturant(models.Model):
    index = models.IntegerField()
    id_no = models.IntegerField(primary_key=True)
    name = models.TextField()
    items = models.TextField()
    lat_long = models.TextField()
    full_details = models.TextField()
