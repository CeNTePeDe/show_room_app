from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from customer.serializer import (
    CustomerSerializer,
    TransactionSerializer,
)
from customer.models import Customer, Transaction
from user.permission import IsCustomerOrReadOnly, IsCarShowroomOrReadOnly


class CustomerView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Display all customers"""

    queryset = Customer.objects.filter(is_active=True).select_related("user")
    serializer_class = CustomerSerializer
    # permission_classes = [IsCustomerOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        car_showroom = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(car_showroom)
        return Response(serializer.data)

    @action(
        detail=True, methods=["delete"], url_path=r"", permission_classes=[IsAdminUser]
    )
    def delete_customer(self, request, pk=None):
        Customer.objects.get(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Transaction.objects.prefetch_related("customer", "car_showroom", "car")
    serializer_class = TransactionSerializer
    # permission_classes = [IsCarShowroomOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        transaction = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(transaction)
        return Response(serializer.data)
