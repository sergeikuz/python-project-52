from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .models import Person



class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = Person.objects.all()[:15]  # или иной способ получить пользователей
        return render(
            request,
            "users/index.html",
            context={"users": users},  # замените соответствующим образом
        )


class UserView(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Person, id=kwargs["id"])
        return render(
            request,
            "users/show.html",
            context={
                "user": user,
            },
        )


def home(request):
    return redirect(reverse('index'))


# Create your views here.
