from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


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
    executor = UserModelChoiceField(
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


class TaskFilter(django_filters.FilterSet):
    my_tasks = django_filters.BooleanFilter(
        field_name='owner',
        label=_("Only my tasks"),
        method='filter_my_tasks',
        widget=forms.CheckboxInput(),
    )

    def filter_my_tasks(self, queryset, name, value):
        if value:  # Если True,фильтруем задачи,где владелец-текущий пол.
            return queryset.filter(owner=self.request.user)
        # Если False, возвращаем все задачи без фильтрации по владельцу.
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'my_tasks']
