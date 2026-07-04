from django.contrib import admin
from django.contrib.auth.models import Group

from task_manager.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "status",
                    "datetime", "expiration_datetime" ]
    list_filter = ["status", "tags"]
    search_fields = ["content"]
    list_per_page = 10


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 10

admin.site.unregister(Group)