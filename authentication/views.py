from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import response, status
from rest_framework.permissions import AllowAny

# Create your views here.

class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return response(serializer.errors)
        
