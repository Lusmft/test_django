import typing

from django.http.request import HttpRequest
from django_filters import rest_framework as overrided_drf_filters

from rest_framework import status, filters, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from .models import User, Channel
from .serializers import LoginSerializer, RegistrationSerializer, ChannelSerializer, Registration2Serializer, Login2Serializer

class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
  

class ChannelListCreateEndpoint(ListCreateAPIView):
    """API endpoint позволяющий просматривать список каналов и создавать их."""

    serializer_class = ChannelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, overrided_drf_filters.DjangoFilterBackend]
    search_fields = ['title']
    queryset = Channel.objects.all()

    def list(self, request: HttpRequest, *args: typing.Any, **kwargs: typing.Any) -> Response:  # noqa: A003
        """
        Возвращает список Каналов.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request: HttpRequest, *args: typing.Any, **kwargs: typing.Any) -> Response:
        """
        Позволяет создать новый Канал.
        """
        return super().create(request, *args, **kwargs)
        

class Registration2APIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = Registration2Serializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class Login2APIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = Login2Serializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)