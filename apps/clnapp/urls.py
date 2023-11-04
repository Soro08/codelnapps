from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include
from clnapp.api.routers import router
from clnapp.views import home

urlpatterns = [
    path("", home, name="home"),
    path("api/", include(router.urls)),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
