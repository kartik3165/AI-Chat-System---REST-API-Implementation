# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, UserProfile

# This serializer handles user registration and profile creation
class UserSerializer(serializers.ModelSerializer):
    # Password should be write-only for security
    password = serializers.CharField(write_only=True)
    # Tokens are read from the associated profile
    tokens = serializers.IntegerField(read_only=True, source='profile.tokens')

    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

    def create(self, validated_data):
        # Create a new user with encrypted password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # The profile will be created automatically through the signal we set up
        return user

# This serializer handles chat message creation and retrieval
class ChatSerializer(serializers.ModelSerializer):
    # Add username field to show who sent the message
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Chat
        fields = ['username', 'message', 'response', 'timestamp']
        # These fields should be read-only as they're set by the system
        read_only_fields = ['response', 'timestamp', 'username']

    def validate_message(self, value):
        # Ensure the message isn't empty
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty")
        return value