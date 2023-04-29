from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from customer.serializer import (
    CustomerSerializer,
    CustomerDetailSerializer,
    TransactionSerializer,
)
from customer.models import Customer, Transaction
from user.permission import IsCustomerOrReadOnly, IsCarShowroomOrReadOnly


class CustomerView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Display all customers"""

    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerDetailSerializer
    permission_classes = (IsAdminUser, IsCustomerOrReadOnly)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


class TransactionView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Transaction.objects.all()

    serializer_class = TransactionSerializer
    permission_classes = [IsCarShowroomOrReadOnly]
