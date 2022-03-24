from django.urls import path
from .views import first

urlpatterns = [
    path('', first, name='homepage'),
    # path('404/', func, name='404'),
    ]