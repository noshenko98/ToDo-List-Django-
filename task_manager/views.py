from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from task_manager.forms import (TaskCreateForm,
                                TagUpdateForTaskForm)
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


class TagUpdateForTaskView(UpdateView):
    model = Task
    form_class = TagUpdateForTaskForm
    success_url = reverse_lazy("task_manager:task-list")


class ChangeStatusTaskView(View):
    model = Task

    def get(self, request, *args, **kwargs):
        if kwargs["status"] == "done":
            task = Task.objects.get(id=kwargs["pk"])
            task.status = True
        else:
            task = Task.objects.get(id=kwargs["pk"])
            task.status = False
        task.save()
        print(Task.objects.get(id=kwargs["pk"]).status)
        return HttpResponseRedirect(reverse_lazy(
            "task_manager:task-list"))
