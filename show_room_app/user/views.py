from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework import viewsets, status, generics
from rest_framework import mixins
from rest_framework.views import APIView

from cars.permission import IsAdminUserOrReadOnly
from user.models import User
from user.serializer import UserSerializer, RegisterSerializer, ChangePasswordSerializer


class UserView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class RegistrationAPIView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
