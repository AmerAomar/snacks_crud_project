from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnackViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.snack = Snack.objects.create(
            title='Test Snack',
            purchaser=self.user,
            description='This is a test snack'
        )

    def test_snack_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'snacks list')

    def test_snack_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.snack.title)

    def test_snack_create_view(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Snack')

    def test_snack_update_view(self):
        url = reverse('snack_update', args=[self.snack.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update Snack')

    def test_snack_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete Snack')

class SnackModelTest(TestCase):
    def test_snack_string_representation(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        snack = Snack.objects.create(
            title='Test Snack',
            purchaser=user,
            description='This is a test snack'
        )
        self.assertEqual(str(snack), 'Test Snack')

    def test_snack_model_fields(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        snack = Snack.objects.create(
            title='Test Snack',
            purchaser=user,
            description='This is a test snack'
        )
        self.assertEqual(snack.title, 'Test Snack')
        self.assertEqual(snack.purchaser, user)
        self.assertEqual(snack.description, 'This is a test snack')
