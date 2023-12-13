from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from rest_framework import viewsets, status, exceptions
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, MeSerializer

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

class MeViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = MeSerializer,

    def list(self, request, *args, **kwargs):
        me = request.user
        return Response({
            "id": me.id,
            "name": me.name,
            "email": me.email
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("GET")
