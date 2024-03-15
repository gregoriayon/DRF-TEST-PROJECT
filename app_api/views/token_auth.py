# Create user auth token using command promt: 'python manage.py drf_create_token user'

# ----- pip install httpie -----
# Using obtain_auth_token url for create user token in command promt: http POST http://127.0.0.1:8000/api/auth/gettoken/ username="user4" password="123456sR"


# Create custom token class generate token for user through url
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_api.models import PersonModel
from app_api.serializers import PersonSerializer



# Basic Authentication & permission class
class TokenAuthView(ListCreateAPIView):
    queryset = PersonModel.objects.all().order_by('-id')
    serializer_class = PersonSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


# Check valid token & get data using: http http://127.0.0.1:8000/api/token/auth/ 'Authorization:Token 4a75c19db2406dec0207bb3a86d395b000e2b047'

# Post on thunder clent:
# {
#   "Authorization": "Token 4a75c19db2406dec0207bb3a86d395b000e2b047",
#   "name": "Mimi",
#   "age": 26
# }