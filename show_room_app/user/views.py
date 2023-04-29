from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import mixins

from cars.permission import IsAdminUserOrReadOnly
from user.models import User
from user.serializer import UserDetailSerializer


class UserView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes =[IsAdminUserOrReadOnly]