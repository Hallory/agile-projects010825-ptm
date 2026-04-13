from rest_framework import status
from rest_framework.decorators import action
from django.utils.timezone import now

from projects.serializers import UserListSerializer, UserDetailSerializer, TaskListSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from projects.models import User, Task

class UserViewSet(ModelViewSet):
    queryset = User.objects.filter()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserDetailSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.deleted_at = now()
        user.is_active = False
        user.save()
        return Response({'detail': 'User has been deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def tasks(self, request, *args, **kwargs):
        user = self.get_object()
        tasks = Task.objects.filter(assignee=user)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            return Response({'detail': "User is already inactive"}, status=status.HTTP_400_BAD_REQUEST)
        user.is_active = False
        user.save(update_fields=['is_active'])
        return Response({'detail': 'User has been deactivated'}, status=status.HTTP_200_OK)