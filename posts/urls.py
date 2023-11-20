from rest_framework import routers
from posts.views.posts import PostViewSet

router = routers.DefaultRouter()
router.register(prefix=r'post', viewset=PostViewSet, basename="Refresh Token")
