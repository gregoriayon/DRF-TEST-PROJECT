from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from app_api.models import PersonModel
from app_api.serializers import PersonSerializer
from app_api.custompermission import CustomPermission
from app_api.customauthentication import CustomAuthentication


# Basic Authentication & permission class
class BasicAuthView(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# Apply custom permission view
class ApplyCustomPermissionView(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    permission_classes = [CustomPermission]



# Apply custom authentication view
class ApplyCustomAuthenticationView(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    