from rest_framework.permissions import BasePermission

# Apply custom permission class
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False
    

    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)