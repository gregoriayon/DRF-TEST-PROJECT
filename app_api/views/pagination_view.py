from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from app_api.models import PlayerModel
from app_api.serializers import PlayerSerializer

from app_api.custom_pagination import CustomPagination, CustomLimitOffsetPagination, CustomCursorPagination


class PaginationView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    pagination_class = CustomPagination

    # pagination_class = PageNumberPagination
    # page_size = 5


class LimitOffsetPaginationView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    pagination_class = CustomLimitOffsetPagination


class CursorPaginationView(ListCreateAPIView):
    queryset = PlayerModel.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    pagination_class = CustomCursorPagination