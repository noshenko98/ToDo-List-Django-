"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from task_manager.views import (TaskListView,
                                TaskCreateView,
                                TaskUpdateView,
                                TaskDeleteView,
                                TagListView,
                                TagCreateView,
                                TagUpdateView,
                                TagDeleteView,
                                TagUpdateForTaskView,
                                ChangeStatusTaskView)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(),
         name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(),
         name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tag/list/", TagListView.as_view(),
         name="tag-list"),
    path("tag/create/", TagCreateView.as_view(),
         name="tag-create"),
    path("tag/update/<int:pk>/", TagUpdateView.as_view(),
         name="tag-update"),
    path("tag/delete/<int:pk>/", TagDeleteView.as_view(),
         name="tag-delete"),
    path("task/update-tag/<int:pk>/", TagUpdateForTaskView.as_view(),
         name="task-update-tag"),
    path("task/update-status/<int:pk>/<str:status>/",
         ChangeStatusTaskView.as_view(),
         name="task-update-status"),
]


app_name = "task_manager"