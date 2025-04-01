from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Existing URL pattern for 'tasks'
    path('', include('tasks.urls')),  # Add this line to make the root URL ('/') go to the tasks URLs
]
