from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet

app_name = UsersConfig.name

rout = DefaultRouter()
rout.register('users', UserViewSet, basename='user')

urlpatterns = [] + rout.urls
