from rest_framework.routers import DefaultRouter
from .viewsets import UsersViewset

router = DefaultRouter()
router.register('user', UsersViewset)