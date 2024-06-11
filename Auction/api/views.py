from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.contrib.auth import authenticate
import random


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.



# Accounts Api 

class LoginApi(APIView):
    def post(self, request):
        data = request.data 
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'error': 'Username & Password Fields is required', 'login': False}, status=status.HTTP_400_BAD_REQUEST)
        

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'login': True,
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials', 'login':False}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterApi(APIView):
    def post(self, request):
        data = request.data 
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)  # Generate JWT token
            return Response({
                'posted': True,
                'id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        elif 'username' in serializer.errors and serializer.errors['username'][0].code == 'unique':
            return Response({"error": "Username already exists", "posted": False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": serializer.errors, "posted": False}, status=status.HTTP_400_BAD_REQUEST)









#apis
class ProductApi(APIView):
    permission_classes = [JWTAuthentication]
    authentication_classes = [JWTAuthentication]


    def get(self, request):
        return Response({
                'payload' : '',
                'Message': 'Success Fetched'
            },
            status=200)
    

