from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from .authentication import CustomTokenObtainPairSerializer
from .views import TodoViewSet
from .auth_views import RegisterView, LoginView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todos/', TodoViewSet.as_view({'get': 'list', 'post': 'create'}), name='todos'),
    path('', include(router.urls)),
]