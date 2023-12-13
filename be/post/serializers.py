from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(source="created_by", read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'body',
            'created_by',
            'user',
            'created_at_formatted'
        ]