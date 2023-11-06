from rest_framework import (
    routers,
)
from .views import (
    UserViewSet,
    Model3dViewSet,
)

router = routers.DefaultRouter()
router.register(
    "users",
    UserViewSet,
    basename="users",
)
router.register(
    "model3d",
    Model3dViewSet,
    basename="model3d",
)
