from .models import FriendshipRequest
from rest_framework import serializers

class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = '__all__'