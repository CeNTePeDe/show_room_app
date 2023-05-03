from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, mixins

from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from car_showroom.models import CarShowRoom, SellModel
from car_showroom.serializer import (
    CarShowRoomSerializer,
    SellModelSerializer,
)
from cars.models import Car
from provider.models import Provider
from user.models import User
from user.permission import IsCarShowroomOrReadOnly


class CarShowRoomView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CarShowRoomSerializer
    queryset = (
        CarShowRoom.objects.filter(is_active=True)
        .prefetch_related("cars")
        .prefetch_related(
            Prefetch('user', queryset=User.objects.all().only('username'))
        )
    )
    permission_classes = [IsCarShowroomOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom = get_object_or_404(queryset, pk=pk)
        serializer = CarShowRoomSerializer(car_showroom)
        return Response(serializer.data)

    @action(
        detail=True, methods=["delete"], url_path=f"", permission_classes=[IsAdminUser]
    )
    def delete_car_showroom(self, request, pk=None):
        CarShowRoom.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellModelView(viewsets.ModelViewSet):
    serializer_class = SellModelSerializer
    queryset = (
        SellModel.objects.prefetch_related("discount")
        .prefetch_related("season_discount")
        .prefetch_related(
            Prefetch('car_showroom', queryset=CarShowRoom.objects.all().only('name'))
        )
        .prefetch_related(
            Prefetch('provider', queryset=Provider.objects.all().only('name'))
        )
        .prefetch_related(
            Prefetch('car', queryset=Car.objects.all().only('name'))
        )
        .all()
    )
    permission_classes = [IsCarShowroomOrReadOnly]
