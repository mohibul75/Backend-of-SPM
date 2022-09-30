import sys

from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from filterData.FilterDataForPrimaryTable import *
from filterData.json_for_3_enspoints import *



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
def slidebar_data(request):
    data = get_slidebar_data()
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

'''@api_view(['GET'])
def technical_indicators_staticis(request):
    data = get_technical_indicators_statistics()
    return Response(data=data)'''

@api_view(['GET'])
def technical_indicators_statistics_of_Company(request, company_code):
    data = get_technical_indicators_statistics_of_Company(company_code)
    if data is None:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return Response(data=data)

@api_view(['GET'])
def historical_data_of_Company(request, company_code):
    data = get_historical_data_of_Company(company_code)
    return Response(data=data)