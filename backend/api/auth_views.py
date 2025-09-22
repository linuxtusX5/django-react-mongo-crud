from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import User, Todo
from .serializers import UserSerializer, RegisterSerializer, TodoSerializer

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=400)

        if not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh), 
            'access': str(refresh.access_token), 
            'user': UserSerializer(user).data
            })

#Todo
class TodoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer