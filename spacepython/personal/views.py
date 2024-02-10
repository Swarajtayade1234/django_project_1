from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializer import DataSerializer

# Create your views here.
@api_view(['GET'])
def data_get(r):
    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def data_post(r):
    serializer =DataSerializer(data=r.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



