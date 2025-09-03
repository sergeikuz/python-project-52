from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "username", "created_at",
                    "updated_at")
    list_filter = ("created_at",)
    search_fields = ("username",)
    ordering = ["-created_at"]
