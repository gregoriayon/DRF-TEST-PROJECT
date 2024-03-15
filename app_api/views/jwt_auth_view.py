from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from app_api.models import PersonModel
from app_api.serializers import PersonSerializer

# Get Token in JWT: http POST http://127.0.0.1:8000/api/token/ username="user4" password="123456sR"
# Refresh Token in JWT: http POST http://127.0.0.1:8000/api/token/refresh/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwOTQ2NzQyMCwiaWF0IjoxNzA5MzgxMDIwLCJqdGkiOiJlMjgzYTY1YTM4Mzg0MzNjYjA4MGFhYWI3NTc4ZjY5YSIsInVzZXJfaWQiOjV9.MVDvKWb27CrYGQU67arXSeq9QXplDz4G7w8i1NmC4WU"
# Verify Token in JWT: http POST http://127.0.0.1:8000/api/token/verify/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MzgwOTUyLCJpYXQiOjE3MDkzODA2NTIsImp0aSI6ImI0MzlhMDgzNDhhYTQ1MGY5OTA0MmRjM2RhMzg4NjMxIiwidXNlcl9pZCI6NX0.bRmYgzLpIS4YWF1xEO2q4XymTmf1UYehiTtwEiIbsgs"

# Get Data: http http://127.0.0.1:8000/api/jwt/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5MzgxODU5LCJpYXQiOjE3MDkzODE1NTksImp0aSI6ImEyMWY5ZjIxNzMyZTQzYTM5OTliN2QxMTE5NDhjOTBjIiwidXNlcl9pZCI6Mn0.q8wI1WryWXkrUnIsp0d6Z5VyNgDr6xz-WKLokt208Ns'


class JWTAuthViewsetAPI(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]