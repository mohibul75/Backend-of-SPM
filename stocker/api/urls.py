from django.urls import path
from .views import *

urlpatterns = [
    path('hellow/', hellow),
    path('spm/', spm),

    path('home_company_data/', home_company_data),
    path('trade_statistics/', trade_staticis),
    path('technical_indicators_staticis/', technical_indicators_staticis),

    path('cat_todays_value/', cat_todays_value),
    path('cat_compare/', cat_compare),
    path('cat_gainer_loser/', cat_gainer_loser)

]