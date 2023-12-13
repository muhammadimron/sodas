from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api, views

router = SimpleRouter()

router.register(r'signup', views.SignupViewsets, basename="signup")
router.register(r'me', views.MeViewsets, basename="me")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
