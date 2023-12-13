from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewsets

router = SimpleRouter()

router.register(r'', PostViewsets, basename='post')

urlpatterns = router.urls
