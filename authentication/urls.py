from django.urls import path
from .views import UserRegistration
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login - get access + refresh tokens
    TokenRefreshView,     # Refresh - get new access token
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegistration.as_view(), name= 'User registration'
         )
]
