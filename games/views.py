from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Games
from .serializers import GameSerializer

# Create your views here.

class GameListView(ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
