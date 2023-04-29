from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from car_showroom.models import CarShowRoom, SellModel
from car_showroom.serializer import (
    CarShowRoomSerializer,
    CarShowRoomDetailSerializer,
    SellModelSerializer,
)
from user.permission import IsCarShowroomOrReadOnly


class CarShowRoomListView(viewsets.ModelViewSet):
    serializer_class = CarShowRoomDetailSerializer
    queryset = CarShowRoom.objects.filter(is_active=True)
    permission_classes =[IsCarShowroomOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CarShowRoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom = get_object_or_404(queryset, pk=pk)
        serializer = CarShowRoomDetailSerializer(car_showroom)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellModelListView(viewsets.ModelViewSet):
    serializer_class = SellModelSerializer
    queryset = SellModel.objects.all()
    permission_classes = [IsCarShowroomOrReadOnly]
