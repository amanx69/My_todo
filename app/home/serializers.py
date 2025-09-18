from  rest_framework import serializers
from .models import Todomodel



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todomodel
        fields = ['id','title', 'description', 'compeleted',"user","created_at","updated_at"]
        
        
        
    def create(self, validated_data):
        user= self.context['request'].user
        todo= Todomodel.objects.create(**validated_data,user=user)
        return todo
    
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.compeleted = validated_data.get('compeleted', instance.compeleted)
        instance.save()
      
        return instance