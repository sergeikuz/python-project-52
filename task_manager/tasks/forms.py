from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

User = get_user_model()


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(attrs={"placeholder": _("Name")})
    )
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"placeholder": _("Description")})
    )
    status = forms.ModelChoiceField(
        label=_("Status"),
        queryset=Status.objects.all(),
        empty_label=None,
        widget=forms.Select()
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_("Executor"),
        empty_label=None,
        widget=forms.Select()
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_("Labels"),
        required=False,
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]



