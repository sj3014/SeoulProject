from rest_framework import permissions


class AdminUserPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        print("TMP1", request.adminUser.uuid)
        print("TMP2", request.data)
        return True
