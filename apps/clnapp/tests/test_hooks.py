from django.contrib.auth.models import (
    User,
)
from django.urls import (
    reverse,
)
from rest_framework import (
    status,
)
from clnapp.tests import (
    TestCase,
)
from clnapp.models import (
    Model3d,
    UserBadge,
)
from clnapp.models.constants import (
    BADGE_COLLECTOR,
)


class Model3dHookTestCase(TestCase):
    def test_add_greater_than_5_model3d(
        self,
    ):
        """
        Adds model3d object and check user has collector badge
        0. The test user has 4 3D models.
        1.
            - Verify that the user has fewer than 5 Model3d objects.
            - Verify that the user does not have the collector badge.
        2. Log in the user.
        3. Add a new model.
        4.
            - Verify that the user has 5 models.
            - Verify that the user has the collector badge.
        """
        user = User.objects.get(username="soro2")

        # befor test
        self.assertNotEqual(
            Model3d.objects.filter(author=user).count(),
            5,
        )
        nb_b = UserBadge.objects.filter(
            user=user,
            badge__name=BADGE_COLLECTOR,
        ).count()
        self.assertFalse(nb_b > 0)

        # --------- beguin test

        # login user with jwt
        data = {
            "username": user.username,
            "password": "AzertyKlm",
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data,
            format="json",
        )
        self.assertEqual(
            login_response.status_code,
            status.HTTP_200_OK,
        )
        login_data = login_response.json()
        access = login_data.get("access")
        # create 4 models
        data = {
            "title": "Model1",
            "description": "Description du modèle 1",
            "file": self.file,
        }
        headers = {"Authorization": f"Bearer {access}"}

        # Créez 5 modèles en envoyant une requête POST répétée
        # for _ in range(5):
        response = self.client.post(
            reverse("model3d-list"),
            data,
            format="multipart",
            headers=headers,
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        # --- After test
        # Vérifiez si 5 modèles ont été créés dans la base de données
        self.assertEqual(
            Model3d.objects.filter(author=user).count(),
            5,
        )
        nb_b = UserBadge.objects.filter(
            user=user,
            badge__name=BADGE_COLLECTOR,
        ).count()
        self.assertTrue(nb_b > 0)

    def test_add_less_than_5_model3d(
        self,
    ):
        """
        Adds model3d object and check user has not collector badge
        0. The test user has 1 3D model.
        1.
            - Verify that the user has fewer than 5 Model3d objects.
            - Verify that the user does not have the collector badge.
        2. Log in the user.
        3. Add a new model.
        4.
            - Verify that the user has fewer than 5 Model3d objects.
            - Verify that the user does not have the collector badge.
        """
        # 0
        user = User.objects.get(username="soro")

        # 1.
        self.assertNotEqual(
            Model3d.objects.filter(author=user).count(),
            5,
        )
        nb_b = UserBadge.objects.filter(
            user=user,
            badge__name=BADGE_COLLECTOR,
        ).count()
        self.assertFalse(nb_b > 0)

        # 2.
        data = {
            "username": user.username,
            "password": "soro",
        }
        login_response = self.client.post(
            reverse("token_obtain_pair"),
            data,
            format="json",
        )
        self.assertEqual(
            login_response.status_code,
            status.HTTP_200_OK,
        )
        login_data = login_response.json()
        access = login_data.get("access")

        # 3
        data = {
            "title": "Model1",
            "description": "Description du modèle 1",
            "file": self.file,
        }
        headers = {"Authorization": f"Bearer {access}"}

        response = self.client.post(
            reverse("model3d-list"),
            data,
            format="multipart",
            headers=headers,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        # 4
        self.assertNotEqual(
            Model3d.objects.filter(author=user).count(),
            5,
        )
        nb_b = UserBadge.objects.filter(
            user=user,
            badge__name=BADGE_COLLECTOR,
        ).count()
        self.assertFalse(nb_b > 0)
