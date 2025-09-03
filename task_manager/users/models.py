from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last name"))
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Username")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='custom_user',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='custom_user',
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def delete(self, *args, **kwargs):
        protected_tasks = self.tasks_owned.all() | self.tasks_executed.all()

        if protected_tasks.exists():
            raise models.ProtectedError(
                "User cannot be deleted because it is in use.",
                protected_tasks
            )
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")