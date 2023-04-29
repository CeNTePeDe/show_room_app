from rest_framework.decorators import permission_classes
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from provider.models import Provider, CarProvider
from provider.serializer import (
    ProviderSerializer,
    ProviderDetailSerializer,
    CarProviderSerializer,
)
from user.permission import IsProviderOrReadOnly


class ProviderListView(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = ProviderDetailSerializer
    queryset = Provider.objects.filter(is_active=True)
    permission_classes = [IsProviderOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProviderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        provider = get_object_or_404(queryset, pk=pk)
        serializer = ProviderDetailSerializer(provider)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarProviderListView(viewsets.ModelViewSet):
    serializer_class = CarProviderSerializer
    queryset = CarProvider.objects.all()
    permission_classes = [IsProviderOrReadOnly]
