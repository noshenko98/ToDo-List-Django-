from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.forms import TaskCreateForm
from task_manager.models import Tag, Task


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 10
    template_name = "task_manager/task_list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    template_name = "task_manager/tag_list.html"

class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")

class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_manager:tag-list")

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("task_manager:tag-list")
