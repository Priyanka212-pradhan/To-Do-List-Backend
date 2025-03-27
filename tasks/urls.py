

from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TaskListCreateView, TaskRetrieveUpdateDeleteView

app_name = 'tasks'

urlpatterns = [
    # Authentication endpoints

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Task API endpoints
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-detail'),
]
