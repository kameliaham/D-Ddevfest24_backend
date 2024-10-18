from django.urls import path
from .views import IsAuthFirstTimeView, CustomTokenObtainPairView, TokenRefreshView, RegisterOperatorView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('register/operator/', RegisterOperatorView.as_view(), name='register_operator'),  
    path('authOperatorFirst', IsAuthFirstTimeView.as_view(), name='authenticatefirst_operator'),  
]