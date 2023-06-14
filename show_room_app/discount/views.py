from requests import Response
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework import mixins
from rest_framework.response import Response

from discount.models import ProviderDiscount, CarShowRoomDiscount
from discount.serializer import (
    ProviderDiscountSerializer,
    CarShowRoomDiscountSerializer,
)
from user.permission import (
    IsProviderDiscountOrReadOnly,
    IsCarShowroomDiscountOrReadOnly,
)


class ProviderDiscountView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ProviderDiscountSerializer
    queryset = ProviderDiscount.objects.filter(is_active=True)
    permission_classes = [IsProviderDiscountOrReadOnly]

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
    viewsets.GenericViewSet,
):
    serializer_class = CarShowRoomDiscountSerializer
    queryset = CarShowRoomDiscount.objects.filter(is_active=True)
    permission_classes = [IsCarShowroomDiscountOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom_discount = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(car_showroom_discount)
        return Response(serializer.data)
