from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.index, name='index'),
    path('piechart/', views.studio_data , name='studio_data'),
    path('piechart2/', views.smaller_studios , name='smaller_studios'),
    path('datetick/', views.number_of_tickets , name='number_of_tickets'),
]