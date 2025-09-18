from rest_framework import viewsets,status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate #! import  for  auth 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed


#! for get tokens for user
def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


#! Sing  up class

class Singup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        data= request.data
        ser =   UserSerializer(data=data)
        if ser.is_valid():
        
            user= ser.save()
            
            token= get_tokens_for_user(user)
            return Response(
                {  
                    "message":"user created successfully",
                    "user":ser.data,
                    "status":status.HTTP_201_CREATED,
                    "token":token
                },
            )
          
        else:
            return Response(
                {
                    "errors":ser.errors,
                    "status":status.HTTP_400_BAD_REQUEST,
                    "messgae ":"something went wrong"
                }
            )
        
     
     # !  login  class  
        
class  Login(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        if not request.data:
            return Response({"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        if 'email' not in request.data or 'password' not in request.data:
            return Response({"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
        
        email= request.data['email']
        password= request.data['password']
        
        user = authenticate(email=email,password=password)
        
        if user is not None:
            refresh= RefreshToken.for_user(user)
            return Response(
                {
                    "refresh":str(refresh),
                    "access":str(refresh.access_token),
                    "message":"login  successfully",
                
            })
        else:
            return Response({"error":"invalid email or password"},status=status.HTTP_400_BAD_REQUEST)
        
        
        
#! for logout
class Logout(APIView):
    pass
    
     
 
        
        

