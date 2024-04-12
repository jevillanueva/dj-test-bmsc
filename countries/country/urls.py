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

]
