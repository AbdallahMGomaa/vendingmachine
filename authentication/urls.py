from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import authentication.views as views

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.UserRegisterView.as_view(), name='register_user'),
]
