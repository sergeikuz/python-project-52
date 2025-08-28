from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class CustomLoginView(LoginView):
    success_message = _("You are logged in")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    success_message = _("You are logged out")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)

class IndexView(TemplateView):
    template_name = "index.html"
