import sys
import os
from django.shortcuts import render

# from os.path import dirname as up
#
# two_up = up(up(__file__))
# # append the path of the parent directory
sys.path.append("..")

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from FilterData.FilterDataForPrimaryTable import *
from FilterData.json_for_3_enspoints import *
from FilterData.health_indicator_script_ak import *
from FilterData.market_summary import *

@api_view(['GET'])
def hellow(request):
    return Response(data={"hellow, welcome to stocker"})


@api_view(['GET'])
def spm(request):
    return Response(data={"hellow, this is spm"})


@api_view(['GET'])
def home_company_data(request):
    data = get_company_statistics()
    return Response(data=data)


@api_view(['GET'])
def trade_staticis(request):
    data = get_trade_statistics()
    return Response(data=data)


@api_view(['GET'])
def cat_todays_value(request):
    data = todays_value()
    return Response(data=data)


@api_view(['GET'])
def cat_compare(request):
    data = compare()
    return Response(data=data)


@api_view(['GET'])
def cat_gainer_loser(request):
    data = gainer_loser()
    return Response(data=data)

@api_view(['GET'])
def technical_indicators_staticis(request):
    data = get_technical_indicators_statistics()
    return Response(data=data)

@api_view(['GET'])
def get_health_indicator(request, company_name):
    data = get_health_indicators(company_name)
    return Response(data=data)

@api_view(['GET'])
def get_market_summary_data(request,company_name):
    data = get_market_summary_datas(company_name)
    return Response(data=data)