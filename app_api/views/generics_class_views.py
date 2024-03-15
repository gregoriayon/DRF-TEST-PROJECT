from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from app_api.serializers import PersonSerializer
from app_api.models import PersonModel


# GenericAPIView & Model Mixin
class GenericPersonListAPIView(GenericAPIView, ListModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class GenericPersonCreateAPIView(GenericAPIView, CreateModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# This class get single person object
class GenericPersonRetrieveAPIView(GenericAPIView, RetrieveModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    


class GenericPersonUpdateAPIView(GenericAPIView, UpdateModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class GenericPersonDeleteAPIView(GenericAPIView, DestroyModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# -------------------------------------------------------------------------------------------------------------

# List & Create Grouping Class
class GenericPersonLCView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# retrieve, update & delete Grouping Class
class GenericPersonRUDView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# -------------------------------------------------------------------------------------------------------------

# GenericAPIView List & Create Class
class GenericListCreate(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer


# GenericAPIView Retrieve, Update & Delete Class
class GenericRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer