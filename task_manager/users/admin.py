from django.contrib import admin
from .models import Person
from django.contrib.admin import DateFieldListFilter


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "created_at",
    )  # Перечисляем поля, отображаемые в таблице списка статей

    search_fields = ["first_name", "last_name"]
    
    list_filter = (
        ("created_at", DateFieldListFilter),
    )  # Перечисляем поля для фильтрации
    

# Register your models here.
