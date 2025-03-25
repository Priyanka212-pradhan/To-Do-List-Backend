from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('register/', views.register, name='register'),  # Your registration page URL
    path('', views.register, name='home'),  # Add this line to handle the root URL
    path('login/', views.user_login, name='login'),
    path('create/', views.create_task, name='create_task'),
    path('logout/', views.user_logout, name='logout'),  # Logout page
    path('tasks/', views.task_list, name='task_list'),  # View all tasks
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit task URL
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Added delete task URL
]
