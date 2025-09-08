from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "executor", "created_at")
    list_filter = ("status", "executor")
    search_fields = ("name",)
