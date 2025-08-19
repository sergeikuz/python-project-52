from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserCRUDTestCase(TestCase):
    def setUp(self):
        # Создаете клиент для свежего общения с сервером
        self.client = Client()
        # Создаете пользователя для тестирования
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user.save()

    def test_user_creation(self):
        # Проверяет создание пользователя
        response = self.client.post(reverse('users:user_create'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        })
        self.assertEqual(response.status_code, 302)  # проверяет, что произошел редирект после успешного создания
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_update(self):
        # Логин от имени пользователя
        self.client.login(username='testuser', password='password')
        
        response = self.client.post(reverse('users:user_update', kwargs={'pk': self.user.pk}), {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()  # обновите объект из базы данных
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete(self):
        # Логин от имени пользователя
        self.client.login(username='testuser', password='password')
        
        response = self.client.post(reverse('users:user_delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
