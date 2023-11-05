from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from clnapp.tests import TestCase
from clnapp.models import Model3d, UserBadge
from clnapp.models.constants import BADGE_COLLECTOR


class RegisterUserTestCase(TestCase):
    def test_create_user(self):
        nb_user_before_add = User.objects.count()
        data = {
            "username": "soro4",
            "email": "kone@gmail.com",
            "first_name": "KONE",
            "last_name": "BEMA",
            "password": "AzertyKlm",
            "password2": "AzertyKlm",
        }

        response = self.client.post(reverse("users-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        nb_user_after_add = User.objects.count()
        self.assertEqual(nb_user_before_add + 1, nb_user_after_add)

    def test_create_user_invalid_data(self):
        nb_user_before_add = User.objects.count()
        data = {
            "email": "kone@gmail.com",
            "first_name": "KONE",
            "last_name": "BEMA",
            "password": "AzertyKlm",
            "password2": "AzertyKlm",
        }

        response = self.client.post(reverse("users-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        nb_user_after_add = User.objects.count()
        self.assertNotEqual(nb_user_before_add + 1, nb_user_after_add)

    def test_get_all_users(self):
        response = self.client.get(reverse("users-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_users(self):
        urls = reverse("users-detail", kwargs={"pk": "1"})
        response = self.client.get(urls, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
