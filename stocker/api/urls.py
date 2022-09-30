from django.urls import path
from .views import *

urlpatterns = [
    path('hellow/', hellow),
    path('spm/', spm),
    path('slidebar/data/', slidebar_data),
    path('home_company_data/', home_company_data),
    path('trade_statistics/', trade_staticis),
    #path('technical_indicators_staticis/', technical_indicators_staticis),
    path('technical_indicators_staticis/<str:company_code>/', technical_indicators_statistics_of_Company),
    path('historical_data_of_Company/<str:company_code>/', historical_data_of_Company),


    path('cat_todays_value/', cat_todays_value),
    path('cat_compare/', cat_compare),
    path('cat_gainer_loser/', cat_gainer_loser)
]