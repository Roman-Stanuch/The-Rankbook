from django.db import models

# Create your models here.

class Ranking(models.Model):
    school = models.ForeignKey("schools.School", on_delete=models.CASCADE, related_name="rankings")
    business = models.CharField(max_length=64)
    type = models.CharField(max_length=16)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.business}"