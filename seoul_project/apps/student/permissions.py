from rest_framework import permissions


class StudentPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        print("TMP1", request.user)
        return True
