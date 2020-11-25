from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile_page, name="profile"),
    path('station_list/', views.StationList.as_view(), name='station_list'),
    path('add_station/', views.station_entry, name='add_station'),
]