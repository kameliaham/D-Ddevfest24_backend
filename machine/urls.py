from django.urls import path
from .views import machine_data_webhook, machine_dashboard


urlpatterns = [
    # The view function `machine_data_webhook` handles the incoming data.
    path('webhook/', machine_data_webhook, name='machine_data_webhook'),
   
    # URL route for the machine dashboard. This route allows users to access the dashboard
    path('dashboard/', machine_dashboard, name='machine_dashboard'),


]