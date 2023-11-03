from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from django.urls import path, include
from clnapp.views import UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
