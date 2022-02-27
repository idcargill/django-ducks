from django.urls import path
from duckburg.views import DuckburgHome

urlpatterns = [
  path('', DuckburgHome.as_view(), name='duckburg')
]
