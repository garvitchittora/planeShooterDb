from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from core.models import leaderboard
from rest_framework.response import Response 
from rest_framework import status
from .serializers import leaderboardSerializer
from rest_framework.views import APIView
def main(request):
   text = """<h1>welcome to my app , this creates API for my game (PLANE SHOOTER) !</h1>"""

   return HttpResponse(text) 

class leaderboardList(APIView):
      def get(self,request):
         leaderboard1=leaderboard.objects.all().order_by('-score')
         serializer=leaderboardSerializer(leaderboard1,many = True)
         return Response(serializer.data)

      def post(self,request):
         try:
            obj = leaderboard.objects.get(name=request.data['name'],score=request.data['score'])
         except leaderboard.DoesNotExist:
            obj = leaderboard(name=request.data['name'],score=request.data['score'])
            obj.save()

         leaderboard1=leaderboard.objects.all()
         serializer=leaderboardSerializer(leaderboard1,many = True)
         return Response(serializer.data)


