from django.urls import path
from tasks.views import TasksListView, TaskPostView, TaskUpdateView

urlpatterns = [
    path('liste', TasksListView.as_view()),
    path('add', TaskPostView.as_view()),
    path('change/<int:id>/', TaskUpdateView.as_view()),
]

