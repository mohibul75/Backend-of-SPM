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
from FilterData.company_short_form_with_name import *
from FilterData.technical_indicator_graph_ifty import *
from FilterData.technical_indicator_dip import *
from FilterData.data_sender_dip import *
from FilterData.cgg_data_sender_dip import *


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

@api_view(['GET'])
def get_health_indicator(request, company_name):
    data = get_health_indicators(company_name)
    return Response(data=data)


@api_view(['GET'])
def get_market_summary_data(request,company_name):
    data = get_market_summary_datas(company_name)
    return Response(data=data)

@api_view(['GET'])
def get_market_summary_graph(request,company_name, datefrom):
    data = market_summary_graph_data(company_name, datefrom)
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


@api_view(['GET'])
def company_short_name(request):
    data = company_short_form_generator()
    return Response(data=data)

@api_view(['GET'])
def movingAverageGraph(request,company_code):
    data = getMovingAverage(company_code)
    return Response(data=data)


@api_view(['GET'])
def MACDgraph(request,company_code):
    data = getMACD(company_code)
    return Response(data=data)


@api_view(['GET'])
def RSIgraph(request, company_code):
    data = getRSI(company_code)
    return Response(data=data)


@api_view(['GET'])
def dY_MACD_PE(request, company_code):
    data = getdY_MACD_PE(company_code)
    return Response(data=data)


@api_view(['GET'])
def bollingerBand(request, company_code):
    data = getBollingerBand(company_code)
    return Response(data=data)


@api_view(['GET'])
def stochastic(request, company_code):
    data = getStochastic(company_code)
    return Response(data=data)


@api_view(['GET'])
def averageDirectionalIndex(request, company_code):
    data = getAverageDirectionalIndex(company_code)
    return Response(data=data)


@api_view(['GET'])
def ovp(request, company_code):
    data = getOBV(company_code)
    return Response(data=data)


@api_view(['GET'])
def candle_graph(request, company_code):
    data = getCandleData(company_code)
    return Response(data=data)


@api_view(['GET'])
def get_cgg_data(request, company_code):
    data = getCCGData(company_code)
    return Response(data=data)


# @api_view(['GET'])
# def last_10_days_update(request):
#     data = Last_ten_days_price_update()
#     return Response(data = data)


# @api_view(['GET'])
# def market_category(request):
#     data = Market_category()
#     return Response(data=data)