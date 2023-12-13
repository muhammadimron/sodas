from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        data = {
            "body": request.data["body"],
            "created_by": request.user.id
        }
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)