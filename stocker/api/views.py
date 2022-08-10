from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from FilterData.FilterDataForPrimaryTable import get_home_comapny_data,get_trade_statistics

@api_view(['GET'])
def hellow(request):
    return Response(status=status.HTTP_200_OK,
                    data={"hellow, welcome to stocker"})


@api_view(['GET'])
def spm(request):
    return Response(status=status.HTTP_200_OK,
                    data={"hellow, this is spm"})


@api_view(['GET'])
def home_company_data(request):
    data = get_home_comapny_data()
    return Response(status=status.HTTP_200_OK, data=data)


@api_view(['GET'])
def trade_staticis(request):
    data = get_trade_statistics()
    return Response(status=status.HTTP_200_OK, data=data)