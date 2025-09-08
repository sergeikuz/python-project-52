from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm, TaskFilter
from task_manager.mixins import CustomLoginRequiredMixin
from django_filters.views import FilterView


class TaskListView(CustomLoginRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/tasks_index.html"
    context_object_name = "tasks"
    filterset_class = TaskFilter

    def get_filterset(self, filterset_class):
        # Передача текущего пользователя в фильтр
        return filterset_class(
            self.request.GET or None,
            queryset=self.get_queryset(),
            request=self.request
        )


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'general_form.html'
    success_url = reverse_lazy("tasks:tasks_index")
    success_message = _("Task created successfully")
    form_title = _("Create task")
    form_submit = _("Create")

    '''def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)'''

    def form_valid(self, form):
        # Вывод отладочной информации
        print(f"Status: {form.cleaned_data['status']}")
        print(f"Executor: {form.cleaned_data['executor']}")
        print(f"Labels: {form.cleaned_data['labels']}")
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'general_form.html'
    success_url = reverse_lazy("tasks:tasks_index")
    success_message = _("Task updated successfully")
    form_title = _("Edit task")
    form_submit = _("Edit")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


class TaskDeleteView(
    CustomLoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Task
    template_name = 'general_delete_form.html'
    success_url = reverse_lazy("tasks:tasks_index")
    success_delete_message = _("Task successfully deleted")
    permission_denied_message = _("A task can only be deleted by its author")
    form_title = _("Delete task")

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if not self.test_func():
            messages.error(
                self.request,
                self.permission_denied_message)
            return redirect(self.success_url)
        messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/tasks_detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.get_object()
        return context
