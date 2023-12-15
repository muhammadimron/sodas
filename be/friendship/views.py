from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from account.models import User
from .models import FriendshipRequest
from .serializers import FriendshipRequestSerializer

class FriendshipRequestViewset(viewsets.GenericViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer

    @action(methods=['POST'], detail=True)
    def requesting(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)

        friendship = FriendshipRequest(created_for=user, created_by=request.user)

        data = self.get_serializer(friendship).data

        return Response(data, status=status.HTTP_200_OK)