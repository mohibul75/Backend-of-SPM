from django.urls import path
from .views import *

urlpatterns = [
    path('hellow/', hellow),
    path('spm/', spm),

    path('home_company_data/', home_company_data),
    path('trade_statistics/', trade_staticis)
]