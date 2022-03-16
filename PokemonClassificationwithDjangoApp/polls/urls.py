from django.urls import path
from django.conf.urls.static import static
from .views import first, func, results

urlpatterns = [
    path('', first, name='homepage'),
    path('404/', func, name='404'),
    path('results/', results, name='results_show'),
    ]