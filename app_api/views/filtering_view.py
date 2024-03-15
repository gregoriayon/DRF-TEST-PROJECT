from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from app_api.models import PlayerModel
from app_api.serializers import PlayerSerializer

from app_api.custom_filter import CustomFilter


class FilterView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'age']


    # def get_queryset(self):
    #     return PlayerModel.objects.filter(age=21)


class SearchFilterView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'age']

    # Lookup: ^	istartswith- Starts-with search.
    # search_fields  = ['^name']



class OrderingFilterView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    filter_backends = [OrderingFilter]
    ordering_fields  = ['name', 'age']


class CustomFilterView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    filter_backends = [CustomFilter]

