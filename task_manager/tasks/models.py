from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name=_("Status")
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="tasks_owned",
        verbose_name=_("Owner")
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="tasks_executed",
        verbose_name=_("Executor")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at"))
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at"))

    def __str__(self):
        return self.name
