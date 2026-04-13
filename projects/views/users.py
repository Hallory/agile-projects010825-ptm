from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from projects.models import User
from projects.serializers.users import UserListSerializer,UserDetailSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserDetailSerializer
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save(update_fields=['is_active'])
        return Response(data={"message": "User was deleted successfully"}, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)