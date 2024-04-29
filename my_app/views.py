from .utils import send_otp
import datetime
from rest_framework.permissions import BasePermission,AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import *

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        print(phone)
        try:
            user = User.objects.get(phone=phone)
            print(user)

            # Check for max OTP attempts
            if int(user.max_otp_try) == 0 and user.otp_max_out and timezone.now() < user.otp_max_out:
                return Response(
                    "Max OTP try reached, try after an hour",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Generate OTP and update user record
            otp = random.randint(1000, 9999)
            otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
            max_otp_try = int(user.max_otp_try) - 1

            user.otp = otp
            user.otp_expiry = otp_expiry
            user.max_otp_try = max_otp_try

            if max_otp_try == 0:
                otp_max_out = timezone.now() + datetime.timedelta(hours=1)
            elif max_otp_try == -1:
                user.max_otp_try = 3
            else:
                user.otp_max_out = None
                user.max_otp_try = max_otp_try

            user.save()

            print(user.otp, 'OTP', user.phone)

            send_otp(user.phone, otp, user)

            return Response("Successfully generated OTP", status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            user_ = User.objects.create(phone=phone)
            print(user_)

            otp = random.randint(1000, 9999)
            otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
            max_otp_try = int(user_.max_otp_try) - 1

            user_.otp = otp
            user_.otp_expiry = otp_expiry
            user_.max_otp_try = max_otp_try

            if max_otp_try == 0:
                otp_max_out = timezone.now() + datetime.timedelta(hours=1)
            elif max_otp_try == -1:
                user_.max_otp_try = 3
            else:
                user_.otp_max_out = None
                user_.max_otp_try = max_otp_try

            user_.is_passenger = True
            user_.save()

            send_otp(user_.phone, otp, user_)

            return Response("Successfully generated OTP", status=status.HTTP_200_OK)
        else:
            return Response("Phone number is incorrect", status=status.HTTP_401_UNAUTHORIZED)

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        otp = request.data['otp']
        print(otp)
        user = User.objects.get(otp=otp)

        if user:
            login(request, user)
            user.otp = None
            user.otp_expiry = None
            user.max_otp_try = 3
            user.otp_max_out = None
            user.save()
            refresh = RefreshToken.for_user(user)

            return Response({'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            return Response("Please enter the correct OTP", status=status.HTTP_400_BAD_REQUEST)