from django.urls import path
from .views import machine_data_webhook


urlpatterns = [
    path('webhook/',machine_data_webhook, name='machine_data_webhook'),

]