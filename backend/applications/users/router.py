from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserApiViewSet, UserView


router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)

urlpatterns = [
    path('me/', UserView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
