from django.urls import path
from .views import IsAuthFirstTimeView, CustomTokenObtainPairView, TokenRefreshView, RegisterOperatorView, AuthenticateFirstTimeView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('register/operator/', RegisterOperatorView.as_view(), name='register_operator'),  
    path('isAuthfirst', IsAuthFirstTimeView.as_view(), name='isauthfirst_operator'),  
    path('authOperatorFirst', AuthenticateFirstTimeView.as_view(), name='authOperator_First'),  
]