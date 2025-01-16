# views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from ChatApp.serializers import UserSerializer, ChatSerializer
from .models import UserProfile, Chat

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Registration successful',
            'token': token.key,
            'tokens_remaining': 4000
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        profile = UserProfile.objects.get(user=user)
        return Response({
            'token': token.key,
            'tokens_remaining': profile.tokens
        })
    return Response({
        'error': 'Invalid credentials'
    }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if profile.tokens < 100:
        return Response({
            'error': 'Insufficient tokens'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        profile.tokens -= 100
        profile.save()
        
        # Replace this with actual AI response logic
        response = f"This is a dummy response to: {request.data['message']}"
        
        chat = Chat.objects.create(
            user=request.user,
            message=request.data['message'],
            response=response
        )
        
        return Response({
            'response': response,
            'tokens_remaining': profile.tokens
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def token_balance(request):
    profile = UserProfile.objects.get(user=request.user)
    return Response({
        'username': request.user.username,
        'tokens_remaining': profile.tokens
    })