from django.urls import path
from .views import Singup ,Login
from rest_framework_simplejwt.views import (
    TokenRefreshView,TokenObtainPairView
)



urlpatterns = [
    path("singup/", Singup.as_view(), name="singup"),
    path("login/", Login.as_view(), name="login"),
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Refresh JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
