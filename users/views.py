from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    partial_update=extend_schema(exclude=True) 
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(id=user.id)
