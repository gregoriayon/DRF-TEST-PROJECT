from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app_api.serializers import PersonModel
from app_api.serializers import PersonSerializer


class PersonAPIView(APIView):
    def get_object(self, pk):
        try:
            return PersonModel.objects.get(id=pk)
        except PersonModel.DoesNotExist:
            raise Http404


    def get(self, request, pk=None,format=None):
        if pk is not None:
            obj = self.get_object(pk)
            serializer = PersonSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        objects = PersonModel.objects.all().order_by('-id')
        if objects:
            serializer = PersonSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'response': 'No data available!'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk=None, format=None):
        obj = self.get_object(pk)
        serializer = PersonSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk=None, format=None):
        obj = self.get_object(pk)
        serializer = PersonSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk=None, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response({'response': 'Delete successfully!'}, status=status.HTTP_204_NO_CONTENT)


