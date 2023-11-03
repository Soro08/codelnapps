from rest_framework import viewsets
from django.contrib.auth.models import User

from clnapp.models import Model3d
from .serializers import (
    Model3dSerializer,
    UserSerializer,
    UserDetailSerializer,
    Model3dDetailSerializer,
)
from .permissions import AuthorOrReadOnly

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return UserDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()


class Model3dViewSet(viewsets.ModelViewSet):
    queryset = Model3d.objects.all()
    serializer_class = Model3dSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return Model3dDetailSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
