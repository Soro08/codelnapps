from clnapp.api.serializers import Model3dSerializer, UserSerializer
from django.contrib.auth.models import User

from clnapp.tests import TestCase
from clnapp.models import Model3d


class SerializerTestCase(TestCase):
    def test_model3d_serializer(self):
        """
        This test is used to check the compliance of our models and serializers to ensure the creation of data via the API
        """
        m3d = Model3d.objects.last()
        # Serialize model3d object
        serializer = Model3dSerializer(instance=m3d)

        # Deserialize model3d serialized data
        data = serializer.data
        data["file"] = self.file

        # Deserialize model3d serialized data
        new_serializer = Model3dSerializer(data=data)

        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())

    def test_user_serializer(self):
        user = User.objects.last()

        # Serialize user object
        serializer = UserSerializer(instance=user)

        # Deserialize user serialized data
        data = serializer.data
        data["username"] = "testuser"
        data["password"] = "AzertyKlm"
        data["password2"] = "AzertyKlm"
        # Deserialize user serialized data
        new_serializer = UserSerializer(data=data)

        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())
