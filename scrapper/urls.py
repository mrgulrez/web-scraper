from django.contrib import admin
from django.urls import path
from .views import extract_data, view_data

urlpatterns = [
    path('', extract_data, name='extract_data'),
    path('view/<int:data_id>/', view_data, name='view_data'),
]
