from rest_framework import serializers
from .models import leaderboard

class leaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=leaderboard
        fields="__all__"