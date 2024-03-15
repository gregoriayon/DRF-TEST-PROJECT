from rest_framework import viewsets

from app_api.models import PersonModel
from app_api.serializers import PersonSerializer


class PersonModelViewsetAPI(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer


# Read only model view set
class PersonReadOnlyModelViewsetAPI(viewsets.ReadOnlyModelViewSet):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer