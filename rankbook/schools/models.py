from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.name}, {self.city}"