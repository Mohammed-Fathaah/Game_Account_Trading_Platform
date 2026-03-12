from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        user=authenticate(username=username,password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh":str(refresh),
                "access":str(refresh.access_token),
            })
        return Response({"error": "Invalid username or password"
                         })
