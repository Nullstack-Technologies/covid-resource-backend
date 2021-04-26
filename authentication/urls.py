from django.urls import path, re_path, include
from fcm_django.api.rest_framework import FCMDeviceCreateOnlyViewSet
from rest_framework.routers import DefaultRouter

from .views import (
    RegistrationView, OTPVerifyView,
    OTPGenerateView, UserView, AddressViewSet,
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('verify/', OTPVerifyView.as_view(), name='otp_verify'),
    path('generate/', OTPGenerateView.as_view(), name='otp_generate'),

    path('user/', UserView.as_view(), name='user_details'),
]

router = DefaultRouter()
router.register(r'address', AddressViewSet)
router.register(r'devices', FCMDeviceCreateOnlyViewSet)
urlpatterns += router.urls
