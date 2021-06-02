from django.db import models

# Create your models here.
class Items(models.Model):    
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return self.item