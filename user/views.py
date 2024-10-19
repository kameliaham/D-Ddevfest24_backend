from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, OperatorRegistrationSerializer, ProfileUpdateSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .permissions import IsManager
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class TokenRefreshView(TokenRefreshView):
    pass


class RegisterOperatorView(generics.CreateAPIView):
    serializer_class = OperatorRegistrationSerializer  
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        print(f"Validated data: {serializer.validated_data}")  

        response_data = serializer.save()  
        temporary_password = response_data.get('temporary_password') 
        response_data['temporary_password'] = temporary_password 
        print("respo_data",response_data)  
        return Response(response_data, status=201)


class IsAuthFirstTimeView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request):
        user = request.user
        user_profile = user.userprofile  

        if user_profile.first_login:
            return Response({
                "detail": "Please change your password and complete your profile."
            }, status=status.HTTP_200_OK)

        return Response({
            "detail": "Successfully authenticated."
        }, status=status.HTTP_200_OK)


class AuthenticateFirstTimeView(APIView):
    permission_classes = [AllowAny]  # Only authenticated users can access this view

    def post(self, request):
        user = request.user
        user_profile = user.userprofile  # Access the user's profile

        if user_profile.first_login:
            serializer = ProfileUpdateSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()

                user_profile.first_login = False
                user_profile.save()

                return Response({
                    "detail": "Profile updated successfully. Password changed and profile completed."
                }, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "detail": "Successfully authenticated."
        }, status=status.HTTP_200_OK)
