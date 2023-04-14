from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)

from cars.models import Car
from cars.serializer import CarListSerializers, CarDitailSerializer, CarCreateSerializer


class CarListView(generics.ListAPIView):
    """Display cars"""

    serializer_class = CarListSerializers

    def get_queryset(self):
        car = Car.objects.filter(is_active=True)
        return car


class CarDetailListView(generics.RetrieveAPIView):
    """Display cars"""

    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarDitailSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class CarCreateView(generics.CreateAPIView, generics.DestroyAPIView):
    """Create model car"""

    serializer_class = CarCreateSerializer
    permission_classes = (IsAdminUser,)
