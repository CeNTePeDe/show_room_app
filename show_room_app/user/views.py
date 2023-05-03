from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import mixins

from cars.permission import IsAdminUserOrReadOnly
from user.models import User
from user.serializer import UserSerializer


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
        car = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(car)
        return Response(serializer.data)
