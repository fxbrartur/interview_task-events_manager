from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [

]

urlpatterns += router.urls
