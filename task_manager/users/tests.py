from django.test import TestCase
from django.urls import reverse
from .models import Person  # Убедитесь имена соответствуют

class UsersTest(TestCase):

    def setUp(self):
        Person.objects.create(first_name="Test", last_name="User")

    def test_users_list(self):
        response = self.client.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)

        # Проверяем наличие данных в контексте шаблона
        self.assertIn("users", response.context)
        users = response.context["users"]

        # Проверяем не пустой ли список пользователей
        self.assertTrue(len(users) > 0)
