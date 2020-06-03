from django.contrib import admin
from .models import leaderboard
# Register your models here.

@admin.register(leaderboard)
class leaderboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')
