from rest_framework.routers import DefaultRouter

from projects.views.users import UserViewSet


router = DefaultRouter()
router.register('', UserViewSet, basename='users')

urlpatterns = []
urlpatterns += router.urls