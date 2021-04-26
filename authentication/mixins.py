from rest_framework.views import APIView
from rest_framework import permissions


class AllowAnyPermissionsMixin(APIView):
    permission_classes = [permissions.AllowAny]


class RegisterThrottleAPIViewMixin(APIView):
    # throttle_scope = 'register'
    pass

class LoginThrottleAPIViewMixin(APIView):
    # throttle_scope = 'login'
    pass
