from django.db import models, transaction
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Name"))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"))

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            if self.tasks_labels.exists():
                raise models.ProtectedError(
                    _("Label is in use and cannot be deleted."),
                    self.tasks_labels.all()
                )
            super().delete(*args, **kwargs)
