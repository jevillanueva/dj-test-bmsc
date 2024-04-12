"""URLs for Country and City"""
from django.urls import path
from . import views

app_name = 'country'

urlpatterns = [
    path('', views.country_index, name='country_index'),
    path('new/', views.country_new, name='country_new'),
    path('<int:country_id>/', views.country_detail, name='country_detail'),
    path('<int:country_id>/delete', views.country_delete, name='country_delete'),
    path('<int:country_id>/edit', views.country_edit, name='country_edit'),
    path('<int:country_id>/cities', views.city_index, name='city_index'),
    path('<int:country_id>/cities/new/', views.city_new, name='city_new'),
    path('<int:country_id>/cities/<int:city_id>/', views.city_detail, name='city_detail'),
    path('<int:country_id>/cities/<int:city_id>/delete', views.city_delete, name='city_delete'),
]
