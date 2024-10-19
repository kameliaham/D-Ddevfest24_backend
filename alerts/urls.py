from django.urls import path

from alerts.views import AlertListView, AlertPostView, AlertDeleteView

urlpatterns = [
    path('liste', AlertListView.as_view()),
    path('add', AlertPostView.as_view()),
    path('delete/<int:id>', AlertDeleteView.as_view())
]
