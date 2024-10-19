from django.urls import path
from .views import machine_data_webhook, machine_dashboard


urlpatterns = [
    path('webhook/', machine_data_webhook, name='machine_data_webhook'),
    path('dashboard/', machine_dashboard, name='machine_dashboard'),


]