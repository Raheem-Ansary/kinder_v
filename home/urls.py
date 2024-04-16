from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [

    path('', views.get_context_data, name='home'),
    path('appointment/', views.appointment, name='appointment')
   
]




