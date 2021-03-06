from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile_page, name="profile"),
    path('station_list/', views.StationList.as_view(), name='station_list'),
    path('add_station/', views.station_entry, name='add_station'),
    path('station/<int:id>/', views.station_entry, name='station_update'),
    path('delete_station/<int:id>', views.station_delete, name='station_delete'),
    path('train_list/', views.TrainList.as_view(), name='train_list'),
    path('add_train/', views.train_entry, name='add_train'),
    path('train/<int:id>/', views.train_entry, name='train_update'),
    path('delete_train/<int:id>/', views.train_delete, name='train_delete'),




]
