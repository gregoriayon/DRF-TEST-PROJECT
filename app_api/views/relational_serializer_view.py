from rest_framework import viewsets

from app_api.models import Singer, Song, StudentsModel
from app_api.serializers import SongSerializer, SingerSerializer, StudentHyperLinkedSerializer


class SingerModelViewsetAPI(viewsets.ModelViewSet):
    queryset = Singer.objects.all().order_by('-id')
    serializer_class = SingerSerializer


class SongModelViewsetAPI(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('-id')
    serializer_class = SongSerializer


class StudentHyperLinkedViewsetAPI(viewsets.ModelViewSet):
    queryset = StudentsModel.objects.all().order_by('-id')
    serializer_class = StudentHyperLinkedSerializer



# $ python manage.py shell
# Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from app_api.serializers import StudentHyperLinkedSerializer
# >>> serializer = StudentHyperLinkedSerializer()
# >>> print(repr(serializer))
# StudentHyperLinkedSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     url = HyperlinkedIdentityField(view_name='app_api:studentsmodel-detail')
#     name = CharField(allow_null=True, max_length=255, required=False)
#     roll = CharField(allow_null=True, max_length=255, required=False)
#     mark = IntegerField(required=False)
#     email = EmailField(allow_null=True, max_length=255, required=False)
#     details = CharField(allow_blank=True, allow_null=True, max_length=255, required=False)
# >>>