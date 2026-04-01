from django.contrib import admin
from django.urls import path

from projects.views.projects import ProjectListCreateApiView
from projects.views.tags import TagListCreateAPIView
from projects.views.tasks import get_all_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectListCreateApiView.as_view()),
    path('tasks/', get_all_tasks),
    path('tags/', TagListCreateAPIView.as_view()),
]
