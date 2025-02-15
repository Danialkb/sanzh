from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

from users.models import User
from users.serializers import CreateUserSerializer, VerifyUserSerializer, CreateTokenSerializer, UpdateUserSerializer, GetUserInfoSerializer
from users.services import UserServicesV1, UserServicesInterface


class UserViewSet(ViewSet):
    user_services: UserServicesInterface = UserServicesV1()

    authentication_classes = (JWTAuthentication,)

    @extend_schema(
        request=CreateUserSerializer,
        responses={
            status.HTTP_201_CREATED: CreateUserSerializer,
            status.HTTP_400_BAD_REQUEST: VerifyUserSerializer,
        }
    )
    def create_user(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.user_services.create_user(data=serializer.validated_data)
        serializer = GetUserInfoSerializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=VerifyUserSerializer,
        responses={status.HTTP_201_CREATED: CreateUserSerializer, status.HTTP_400_BAD_REQUEST: None},
    )
    def verify_user(self, request, *args, **kwargs):
        serializer = VerifyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.user_services.verify_user(data=serializer.validated_data)
        if user is None:
            return Response({"detail": "Verification failed"}, status=status.HTTP_400_BAD_REQUEST)

        user_data = CreateUserSerializer(user).data

        return Response(user_data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=CreateTokenSerializer,
        responses={status.HTTP_200_OK: None, status.HTTP_403_FORBIDDEN: None}
    )
    def create_token(self, request, *args, **kwargs):
        serializer = CreateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = self.user_services.create_token(data=serializer.data)

        if tokens is None:
            return Response({"detail": "Invalid username or password"}, status=status.HTTP_403_FORBIDDEN)

        return Response(tokens)

    @extend_schema(
        responses={status.HTTP_200_OK: GetUserInfoSerializer}
    )
    def get_user(self, request, *args, **kwargs):
        user_from_db = User.objects.get(id=request.user.id)
        user = GetUserInfoSerializer(user_from_db)

        return Response(user.data)

    @extend_schema(
        request=UpdateUserSerializer,
        responses={status.HTTP_200_OK: GetUserInfoSerializer}
    )
    def update_user(self, request, *args, **kwargs):
        serializer = UpdateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.user_services.update_user(data=serializer.data, user_id=request.user.id)
        user = GetUserInfoSerializer(user)

        return Response(user.data)
