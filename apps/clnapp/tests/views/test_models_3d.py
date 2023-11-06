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
)


class Models3dTestCase(TestCase):
    def test_get_model3d(
        self,
    ):
        response = self.client.get(
            reverse("model3d-list"),
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_single_model3d(
        self,
    ):
        m3d = Model3d.objects.last()

        urls = reverse(
            "model3d-detail",
            kwargs={"pk": m3d.id},
        )
        response = self.client.get(
            urls,
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            response.json().get("nb_views"),
            m3d.nb_views + 1,
        )
