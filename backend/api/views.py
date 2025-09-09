from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import User, Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Item.objects.filter(created_at=user_id)

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(created_at=user)