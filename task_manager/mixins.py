from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.db import models


class CustomLoginRequiredMixin(LoginRequiredMixin):
    permission_denied_message = _("You are not logged in! Please log in")
    login_url = reverse_lazy("login")
    redirect_field_name = None

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
        return super().handle_no_permission()

