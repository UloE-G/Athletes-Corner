from django.db import models

# Create your models here.


class Newsletter(models.Model):
    email = models.CharField(max_length=254)
