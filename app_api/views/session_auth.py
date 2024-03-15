from django.http import Http404
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from app_api.serializers import PersonModel
from app_api.serializers import PersonSerializer

# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Get session ID
            session_id = request.session.session_key
            # Return response with session ID
            return Response({'message': 'Login successful', 'session_id': session_id}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Using session authentication in class
class SessionAuthView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
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
