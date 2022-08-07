from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hellow(request):
    return Response(status=status.HTTP_200_OK,
                    data={"hellow, welcome to stocker"})


@api_view(['GET'])
def spm(request):
    return Response(status=status.HTTP_200_OK,
                    data={"hellow, this is spm"})