from django.db.models import Prefetch
from rest_framework.decorators import action
from rest_framework import viewsets, status, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from provider.models import Provider, CarProvider
from provider.serializer import (
    ProviderSerializer,
    CarProviderSerializer,
)
from user.permission import IsProviderOrReadOnly


class ProviderView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Provider.objects.prefetch_related("cars", "user").filter(is_active=True)
    serializer_class = ProviderSerializer
    permission_classes = [IsProviderOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(car_showroom)
        return Response(serializer.data)

    @action(
        detail=True, methods=["delete"], url_path=r"", permission_classes=[IsAdminUser]
    )
    def delete_provider(self, request, pk=None):
        Provider.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarProviderListView(viewsets.ModelViewSet):
    serializer_class = CarProviderSerializer
    queryset = CarProvider.objects.prefetch_related("provider", "car")
    permission_classes = [IsProviderOrReadOnly]
