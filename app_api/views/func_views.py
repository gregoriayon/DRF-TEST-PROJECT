from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response


# from django.shortcuts import render
# from io import BytesIO
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt


from app_api.models import StudentsModel, EmployeeModel
from app_api.serializers import StudentsSerializer, EmployeeSerializer

# Create your views here.


def index_view(request):
    return HttpResponse("Test Message!")

def get_students_list_view(request):
    students = StudentsModel.objects.all().order_by('-id')
    serializer = StudentsSerializer(students, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_student_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = StudentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        
    return Response({'status': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def get_employee_view(request, pk):
    employee = get_object_or_404(EmployeeModel, id=pk)

    if employee:
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
    
    return Response({'status': 'errors' }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_employee_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        
    return Response({'status': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'PATCH'])
def update_employee_view(request, pk):
    try:
        obj = get_object_or_404(EmployeeModel, id=pk)
    except EmployeeModel.DoesNotExist:
        return Response({'status': 'Object does not exist!' }, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data
        serializer = EmployeeSerializer(data=data, instance=obj)

    elif request.method == 'PATCH':
        data = request.data
        serializer = EmployeeSerializer(data=data, partial=True, instance=obj)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
        
    return Response({'status': serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
    

