from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.mixins import RegisterThrottleAPIViewMixin, AllowAnyPermissionsMixin
from authentication.permissions import IsCustomer
from authentication.serializers import RegistrationSerializer, VerifyOTPSerializer, RequestOTPSerializer, \
    ProfileSerializer, AddressSerializer
from generic.models import Address


class RegistrationView(CreateAPIView, RegisterThrottleAPIViewMixin, AllowAnyPermissionsMixin):
    """
        This View performs Registration of
        a Customer into the system.
    """
    serializer_class = RegistrationSerializer


class OTPVerifyView(CreateAPIView, RegisterThrottleAPIViewMixin, AllowAnyPermissionsMixin):
    """
        This View performs OTP Authentication of
        a person in the system
    """
    serializer_class = VerifyOTPSerializer


class OTPGenerateView(CreateAPIView, RegisterThrottleAPIViewMixin, AllowAnyPermissionsMixin):
    """
        This View performs OTP Generation/Re-Generation of
        a person in the system
    """
    serializer_class = RequestOTPSerializer


class UserView(RetrieveAPIView):
    """
        This View tries to fetch the current user
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.customer


class LogoutView(CreateAPIView, RegisterThrottleAPIViewMixin):
    """
        Log Out a user from the system
    """

    serializer_class = ProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
        Add/ Update / Delete Address
    """

    serializer_class = AddressSerializer
    queryset = Address.active.all()
    pagination_class = None
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deactivate()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


