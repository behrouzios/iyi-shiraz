from django.urls import path
from .views import ChartDataView, Dcs1hChartDataViewFilter, ChartDataViewHaftegiChart4Data

urlpatterns = [
    path('chart-data/dcs1h-chart_data', ChartDataView.as_view(), name='chart-data-dcs1h-chart_data'),
    path('chart-data-filter/dcs1h-chart-data', Dcs1hChartDataViewFilter.as_view(), name='chart-data-filter-dcs1h-chart_data'),
    path('chart-data-filter/haftegi-chart4-data', ChartDataViewHaftegiChart4Data.as_view(), name='haftegi-chart4-data-filter')

]





