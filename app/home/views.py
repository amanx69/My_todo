from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todomodel
from rest_framework.permissions import IsAuthenticated
import datetime


#! fro  get  login user  

class Userdata(APIView):
    parser_classes = [IsAuthenticated]
    def get(self, request, ):
        todo = Todomodel.objects.filter(user=request.user)
        serializer = TodoSerializer(todo, many=True)
        return Response({
            
            "status":status.HTTP_200_OK,
            "data":serializer.data,
            "message":"success"
        })

#! create todo         
        
class CreateTodo(APIView):
    premmission_classes=[IsAuthenticated]
    def post(self, request, ):
        data= request.data
        user= request.user
        ser=TodoSerializer(data=data,user=user)
        if ser.is_valid():
            ser.save()
            
            return Response({
                "status":status.HTTP_200_OK,
                "data":ser.data,
                "message":"success"
         
            })
                
        else:
            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "data":ser.errors,
                "message":"something went wrong"
            })
            
#! deleted  
class DeleteTodo(APIView):
    premmission_classes=[IsAuthenticated]
    def delete(self, request, id):
    
        try:
            
            todo=  Todomodel.objects.get(id=id)
            if todo.user != request.user:
                return Response({
                
                 "error":"only deleted  own todo"
            })
            todo.delete()
        
            return Response({
            "status":status.HTTP_200_OK,
            "message":"deleted"
        })        
                
        except todo.DoesNotExist:
            return Response({
            "status":status.HTTP_404_NOT_FOUND,
             "error":"error"
        })
            
#! fo update             
class UpdateTodo(APIView):
    premmission_classes=[IsAuthenticated]
    def patch(self, request, id):
        try:
            todo=Todomodel.objects.get(id=id)
            if todo.user!=request.user:
                return Response({
                    "error":"only deleted  own todo"
                })
                
            ser= TodoSerializer(instance=todo,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                todo.updated_at=datetime.datetime.now()
                return Response({
                    "status":status.HTTP_200_OK,
                    "data":ser.data,
                    "message":"success",
                    "name":request.user.email,
                })
            else:
                return Response({
                    "status":status.HTTP_400_BAD_REQUEST,
                    "data":ser.errors,
                    "message":"something went wrong"
                })
        except Todomodel.DoesNotExist:
            return Response({
                "status":status.HTTP_404_NOT_FOUND,
                "error":"todo not found "
            })        
            
            
   