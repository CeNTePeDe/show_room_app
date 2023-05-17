from django.db.models import Prefetch

from rest_framework import viewsets, status, mixins

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from car_showroom.models import CarShowRoom, SellModel
from car_showroom.serializer import (
    CarShowRoomSerializer,
    SellModelSerializer,
)
from user.permission import IsCarShowroomOrReadOnly


class CarShowRoomView(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CarShowRoomSerializer
    queryset = CarShowRoom.objects.filter(is_active=True).prefetch_related(
        "cars", "user"
    )
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom = get_object_or_404(queryset, pk=pk)
        serializer = CarShowRoomSerializer(car_showroom)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     if  request.user.is_authenticated:
    #         car_showroom = self.request.data
    #         serializer = self.serializer_class(data=car_showroom)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_403_FORBIDDEN)

    @action(
        detail=True, methods=["delete"], url_path=f"", permission_classes=[IsAdminUser]
    )
    def delete_car_showroom(self, request, pk=None):
        CarShowRoom.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellModelView(viewsets.ModelViewSet):
    serializer_class = SellModelSerializer
    queryset = SellModel.objects.prefetch_related(
        "discount", "season_discount", "car_showroom", "provider", "car"
    )
