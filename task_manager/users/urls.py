from django.urls import path

from . import views
from task_manager.users.views import IndexView, UserView

app_name = 'users'  # Это указывает, что пространство имен для этого набора путей будет 'users'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:id>/", UserView.as_view(), name="user_show"),
]
