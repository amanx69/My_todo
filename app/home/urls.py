from  django.urls import path
from .views import  *


urlpatterns = [
    path("alldata/",Userdata.as_view(),name="alldata"),
    path("create/",CreateTodo.as_view(),name="create"),
    path("delete/<int:id>/",DeleteTodo.as_view(),name="create"),
    path("update/<int:id>/",UpdateTodo.as_view(),name="update"),
    
]
