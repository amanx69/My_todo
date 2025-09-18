from django.db import models
from users.models import User

# Create your models here.
class Todomodel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='todo_owner',default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    compeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title
    