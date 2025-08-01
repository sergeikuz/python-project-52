from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "users/index.html",
        context={"tags": tags},
    )

# Create your views here.
