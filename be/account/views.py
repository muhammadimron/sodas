from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

class SignupViewsets(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        if mutable_data["password1"] == mutable_data["password2"]:
            mutable_data["password"] = make_password(mutable_data["password1"])
            del mutable_data["password1"]
            del mutable_data["password2"]
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)