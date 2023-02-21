from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Client_Table_Serializer,UserSerializer,Artist_Table_Serializer,Work_Table_Serializer
from .models import *
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = client_table.objects.all()

#     serializer_class = Client_Table_Serializer

class WorkViewSet(ListAPIView):
    
    serializer_class = Work_Table_Serializer
    queryset = Work_table.objects.all()
    filterset_fields = ['work_type']

class ArtistViewSet(ListAPIView):
    queryset = Artist_table.objects.all()
    serializer_class = Artist_Table_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    

class UserViewSet(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()

    return Response("done")

@api_view(['POST'])
def CreateArtist(request):
    serializer = Artist_Table_Serializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def CreateClient(request):
    serializer = Client_Table_Serializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def CreateWork(request):
    serializer = Work_Table_Serializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def Clients(request):
    client = client_table.objects.all()

    serializer = Client_Table_Serializer(client,many=True)
    return Response(serializer.data)