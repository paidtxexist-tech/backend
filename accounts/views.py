from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """регистрация"""
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Поля username и password обязательны'}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь уже существует'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    return Response({'id': user.id, 'username': user.username}, status=201)