from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from FilterData.FilterDataForPrimaryTable import get_home_comapny_data,get_trade_statistics
from FilterData.json_for_3_enspoints import *

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

@api_view(['GET'])
def technical_indicators_staticis(request):
    data = get_technical_indicators_statistics()
    return Response(data=data)

@api_view(['GET'])
def cat_todays_value(request):
    data = todays_value()
    return Response(status=status.HTTP_200_OK, data=data)


@api_view(['GET'])
def cat_compare(request):
    data = compare()
    return Response(status=status.HTTP_200_OK, data=data)


@api_view(['GET'])
def cat_gainer_loser(request):
    data = gainer_loser()
    return Response(status=status.HTTP_200_OK, data=data)