from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm
from django.contrib import messages
from task_manager.mixins import (
    CustomLoginRequiredMixin,
)


class StatusesIndexView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses_index.html"
    context_object_name = "statuses"


class StatusesCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/statuses_form.html'
    success_url = reverse_lazy("statuses:statuses_index")
    success_message = _("The status was created successfully")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class StatusesUpdateView(CustomLoginRequiredMixin, UpdateView):
    form_class = StatusForm
    model = Status
    template_name = 'statuses/statuses_form.html'
    success_url = reverse_lazy("statuses:statuses_index")
    success_message = _("The status was updated successfully")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class StatusesDeleteView(
    CustomLoginRequiredMixin,
    DeleteView
):
    model = Status
    template_name = 'statuses/statuses_confirm_delete.html'
    success_url = reverse_lazy("statuses:statuses_index")
    success_delete_message = _("The status was deleted successfully")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_delete_message)
        return response
