from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import LabelForm
from task_manager.mixins import CustomLoginRequiredMixin


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels_index.html"
    context_object_name = "labels"


class LabelCreateView(CustomLoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/labels_form.html"
    success_url = reverse_lazy("labels:labels_index")
    success_message = _("Label created successfully")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class LabelUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy("labels:labels_index")
    template_name = "labels/labels_form.html"
    success_message = _("Label updated successfully")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class LabelDeleteView(
    CustomLoginRequiredMixin,
    DeleteView
):
    model = Label
    template_name = "labels/labels_confirm_delete.html"
    success_url = reverse_lazy("labels:labels_index")
    success_delete_message = _("Label deleted successfully")

    def form_valid(self, form):
        messages.success(self.request, self.success_delete_message)
        return super().form_valid(form)
