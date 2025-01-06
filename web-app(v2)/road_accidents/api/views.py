from django.shortcuts import render
from rest_framework import viewsets
from .models import Accident
from .serializers import AccidentSerializer

# Create your views here.

class AccidentViewSet(viewsets.ModelViewSet):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer