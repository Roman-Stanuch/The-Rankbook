from django.contrib import admin

from .models import Ranking, RankingCategory

# Register your models here.

admin.site.register(Ranking)
admin.site.register(RankingCategory)