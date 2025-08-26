from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from task_manager.mixins import CustomLoginRequiredMixin


class TaskListView(CustomLoginRequiredMixin, ListView,):
    model = Task
    template_name = "tasks/tasks_index.html"
    context_object_name = "tasks"


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks_form.html'
    success_url = reverse_lazy("tasks:tasks_index")

    success_message = _("Task created successfully")
    error_message = _("Please correct the errors below.")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks_form.html'
    success_url = reverse_lazy("tasks:tasks_index")
    success_message = _("Task updated successfully")
    error_message = _("Please correct the errors below.")

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
    template_name = 'tasks/tasks_confirm_delete.html'
    success_url = reverse_lazy("tasks:tasks_index")
    success_delete_message = _("Task successfully deleted")

    def test_func(self):
        return self.request.user == self.get_object().owner

    def handle_no_permission(self):
        if not self.test_func():
            messages.error(
                self.request,
                _("A task can only be deleted by its author."))
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
