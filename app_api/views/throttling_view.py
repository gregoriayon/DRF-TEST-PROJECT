from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from app_api.models import PersonModel
from app_api.serializers import PersonSerializer
from app_api.custom_throttles import CustomThrottlingRate


class ThrottlesView(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class CustomThrottlesView(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomThrottlingRate]


# CRUD part by part throttling using ScopedRateThrottle
class ScopedLCThrottlesView(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope  = 'LC'


class ScopedRUDThrottlesView(RetrieveUpdateDestroyAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope  = 'RUD'