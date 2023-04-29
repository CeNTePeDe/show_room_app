from requests import Response
from rest_framework import viewsets, status
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
from user.permission import IsCarShowroomOrReadOnly, IsProviderOrReadOnly


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
        serializer = SeasonDiscountSerializer(season_discount)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = SeasonDiscountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


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
