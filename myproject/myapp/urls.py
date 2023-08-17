from django.urls import path
from.views import home, index, nisa

urlpatterns = [
    path('index/', index),
    path("name/jon/", nisa),
    path('', home)
]