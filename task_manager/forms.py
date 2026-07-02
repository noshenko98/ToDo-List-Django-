from django import forms
from task_manager.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "expiration_datetime": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
        }

class TagUpdateForTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }