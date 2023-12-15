from rest_framework.routers import SimpleRouter
from .views import FriendshipRequestViewset

router = SimpleRouter()

router.register(r'', FriendshipRequestViewset)

urlpatterns = router.urls
