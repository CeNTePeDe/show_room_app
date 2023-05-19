from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    GenericAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework import viewsets, status, generics, response
from rest_framework import mixins
from rest_framework_simplejwt.tokens import RefreshToken

from cars.permission import IsAdminUserOrReadOnly
from user.models import User
from user.serializer import (
    UserSerializer,
    UserRegisterationSerializer,
    ChangePasswordSerializer,
    UserLoginSerializer,
)


class UserView(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUserOrReadOnly]

    def retrieve(self, request, pk=id, *args, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class RegistrationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    serializer_class = UserRegisterationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserAPI(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Get, Update user information
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request):
        user = request.user

        serializer = UserSerializer(user)

        return response.Response(serializer.data)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user profile
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.id


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
