from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from cars.models import Car
from cars.permission import IsAdminUserOrReadOnly
from cars.serializer import CarSerializer
from cars.services import CarFilter


class CarView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(car)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get", "post"],
        permission_classes=[IsAdminUser],
        url_path=r"",
    )
    def inactive_cars(self, request):
        inactive = Car.objects.filter(is_active=False)
        self.serializer = CarSerializer(inactive, many=True)
        serializer = self.serializer
        return Response(serializer.data)

    @action(
        detail=True, methods=["delete"], url_path=r"", permission_classes=[IsAdminUser]
    )
    def delete_car(self, request, pk=None):
        Car.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
