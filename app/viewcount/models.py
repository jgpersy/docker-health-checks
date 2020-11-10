from django.db import models

# Create your models here.
class Viewcount(models.Model):
    visits = models.IntegerField(default=0)
    