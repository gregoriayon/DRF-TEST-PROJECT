from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


from app_api.models import PersonModel
from app_api.serializers import PersonSerializer

# viewsets class crud operations

class PersonViewsetAPI(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return PersonModel.objects.get(id=pk)
        except PersonModel.DoesNotExist:
            raise Http404
        
    
    def list(self, request):
        print('----------List----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        objects = PersonModel.objects.all().order_by('-id')
        if objects is not None:
            serializer = PersonSerializer(objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'response': 'No data available!'}, status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self, request, pk=None):
        print('----------Retrieve----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        if pk is not None:
            obj = self.get_object(pk)
            serializer = PersonSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'response': 'No data available!'}, status=status.HTTP_400_BAD_REQUEST)
    

    def create(self, request):
        print('----------Create----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        print('----------Update----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        obj = self.get_object(pk)
        serializer = PersonSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def partial_update(self, request, pk=None):
        print('----------Partial Update----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        obj = self.get_object(pk)
        serializer = PersonSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):
        print('----------Destroy----------')
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name", self.name)
        print("Description", self.description)

        obj = self.get_object(pk)
        obj.delete()
        return Response({'response': 'Delete successfully!'}, status=status.HTTP_204_NO_CONTENT)