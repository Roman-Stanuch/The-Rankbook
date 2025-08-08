from django.db import models

# Create your models here.

class RankingCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Ranking(models.Model):
    category = models.ForeignKey(RankingCategory, on_delete=models.CASCADE, related_name="rankings", null=True)
    school = models.ForeignKey("schools.School", on_delete=models.CASCADE, related_name="rankings")
    business = models.CharField(max_length=64)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.business}"