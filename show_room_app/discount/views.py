from requests import Response
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework import mixins
from rest_framework.response import Response

from cars.permission import IsAdminUserOrReadOnly
from discount.models import SeasonDiscount, ProviderDiscount
from discount.serializer import (
    SeasonDiscountSerializer,
    ProviderDiscountSerializer,
    CarShowRoomDiscountSerializer,
)


class SeasonDiscountView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = SeasonDiscount.objects.all()
    serializer_class = SeasonDiscountSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        season_discount = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(season_discount)
        return Response(serializer.data)


class ProviderDiscountView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProviderDiscountSerializer
    queryset = ProviderDiscount.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        provider_discount = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(provider_discount)
        return Response(serializer.data)


class CarShowRoomDiscountView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CarShowRoomDiscountSerializer
    queryset = SeasonDiscount.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom_discount = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(car_showroom_discount)
        return Response(serializer.data)