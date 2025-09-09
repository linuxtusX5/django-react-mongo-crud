from rest_framework import generics
from rest_framework.response import Response
from rest_framework.rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.view import APIView
from .models import User
from .serializers import UserSerializer, RegisterSerializer

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects
    serializer_class = RegisterSerializer

# Login
class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=400)

        if not user.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh), 
            'access': str(refresh.access_token), 
            'user': UserSerializer(user).data
            })
