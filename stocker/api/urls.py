from django.urls import path
from .views import *

urlpatterns = [
    path('hellow/', hellow),
    path('spm/', spm),
]