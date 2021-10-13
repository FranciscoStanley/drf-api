from .models import Cliente
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

