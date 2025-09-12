from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import User, Item

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ItemSerializer(DocumentSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'created_at']