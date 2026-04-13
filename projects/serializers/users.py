from rest_framework import serializers

from projects.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'role', 'gender', 'age']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['id','date_joined','last_login']
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'role', 'gender', 'age', 'project']

class UserDeleteSerializer(serializers.ModelSerializer):
    pass
