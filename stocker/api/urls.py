from django.urls import path
from .views import *

urlpatterns = [
    path('hellow/', hellow),
    path('spm/', spm),

    path('home_company_data/', home_company_data),
    path('trade_statistics/', trade_staticis),
    # path('technical_indicators_staticis/', technical_indicators_staticis),

    path('cat_todays_value/', cat_todays_value),
    path('cat_compare/', cat_compare),
    path('cat_gainer_loser/', cat_gainer_loser),

    path('health_indicator/<str:company_name>/', get_health_indicator),

    path('market_summary/<str:company_name>/', get_market_summary_data),
    path('get_market_summary_graph/<str:company_name>/<str:datefrom>/', get_market_summary_graph),


    path('technical_indicators_staticis/<str:company_code>/', technical_indicators_statistics_of_Company),
    path('historical_data_of_Company/<str:company_code>/', historical_data_of_Company),

    path('all_company_short_name', company_short_name)
]