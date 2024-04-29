from django.urls import path
from .views import LoginView, VerifyOTPView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]