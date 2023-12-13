from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password'
        ]

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"