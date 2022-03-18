from django.urls import path
from .views import Attrition_rate_finder

urlpatterns = [
    path('show_attrition/', Attrition_rate_finder, name='attrition_show'),
    # path('results-attrition/', results, name='results_show'),
    ]