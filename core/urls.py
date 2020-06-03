from .views import main ,leaderboardList
from django.urls import path

urlpatterns = [
    path('',main),
    path('list',leaderboardList.as_view())
]

