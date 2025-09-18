from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
import  re 
class UserSerializer(serializers.ModelSerializer):
 
 
   
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "created_at"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        user.save()
        return user
    
    
    #! object keable  validate



     
        
        #! if  email exit and username exit  than raise error
     
    
    #! single levle  user  name  validate 

        #! password validation
        
    def validate_password(self, value):
        if len(value)<6 :
            raise serializers.ValidationError("password  must be at  least 6 char long")   
        
        elif  not re.search("[A-Z]",value):
            raise serializers.ValidationError("password  must be  constin  at least  one  uppercase  letter")
        
        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        
        
        return value
        
         #! elmail validation
        
    def validate_email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Invalid email format.")
        return value

    

        
