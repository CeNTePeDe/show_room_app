from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import mixins

from rest_framework.response import Response

from cars.models import Car
from cars.permission import IsAdminUserOrReadOnly
from cars.serializer import CarSerializer, CarListSerializer


class CarListView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CarListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car = get_object_or_404(queryset, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
