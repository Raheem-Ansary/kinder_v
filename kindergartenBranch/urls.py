from django.urls import path
from . import views

urlpatterns = [
    path('branches/', views.branches_view, name='branches_view'),
]
