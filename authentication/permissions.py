from rest_framework import permissions
from rolepermissions.checkers import has_role


class IsCustomer(permissions.BasePermission):
    """
        Permission to Determine whether person is a customer or not
    """

    def has_permission(self, request, view):
        return has_role(request.user, 'customer')


class IsAdmin(permissions.BasePermission):
    """
        Permission to Determine whether person is a customer or not
    """

    def has_permission(self, request, view):
        return has_role(request.user, 'admin')
