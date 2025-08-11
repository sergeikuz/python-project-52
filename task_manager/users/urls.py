from django.urls import path

from . import views
from task_manager.users.views import (
        IndexView,
        UserView,
        LoginUserView,
        UserFormEditView,
)

app_name = 'users'  # Это указывает, что пространство имен для этого набора путей будет 'users'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:id>/", UserView.as_view(), name="user_show"),
    path("create/", LoginUserView.as_view(), name="user_create"),
    path("<int:id>/edit/", UserFormEditView.as_view(), name="user_update"),
]
