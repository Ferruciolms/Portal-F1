from django.urls import path, re_path
from analytics.views.sistem import SistemIndexView
from analytics.views.driver import DriverList, DriverSeasonDetailAPIView
from analytics.views.driver import DriverDetailView
from analytics.views.driver import DriverDetailAPIView
from analytics.views.circuit import CircuitList
from analytics.views.circuit import CircuitDetailAPIView, CircuitDetailView

urlpatterns = [
    path('analytics', SistemIndexView.as_view(), name="analytics"),
    path('analytics/list/driver', DriverList.as_view(), name='driver_list'),
    path('analytics/list/circuit', CircuitList.as_view(), name='circuit_list'),
    path('driver/<int:pk>/detail', DriverDetailView.as_view(), name='detail'),
    path('circuit/<int:pk>/circuit_detail', CircuitDetailView.as_view(), name='circuit_detail'),

    re_path(r'^api/driver/detail/year/$', DriverDetailAPIView.as_view(), name='api_driver_detail_year'),
    re_path(r'^api/driver/detail/season/$', DriverSeasonDetailAPIView.as_view(), name='api_driver_detail_season'),
    re_path(r'^api/circuit/detail/season/$', CircuitDetailAPIView.as_view(), name='api_circuit_detail_season'),
]
