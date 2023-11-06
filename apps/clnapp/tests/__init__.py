from django.test import (
    TestCase as DjangoTestCase,
)
from rest_framework.test import (
    APIClient,
)
import io
from django.core.files.uploadedfile import (
    SimpleUploadedFile,
)


class TestCase(DjangoTestCase):
    fixtures = [
        "users.json",
        "model3d.json",
        "badges.json",
        "userbadges.json",
    ]

    def setUp(self):
        self.client = APIClient()
        file_content = b"Contenu du fichier"
        self.file = SimpleUploadedFile(
            "model1.stl",
            file_content,
        )
