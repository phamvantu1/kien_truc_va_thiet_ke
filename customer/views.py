# from django.shortcuts import render
#
# # Create your views here.


from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.contrib.auth.models import User

from customer.models import customerUser  # ✅ ĐÚNG
from .serializers import UserSerializer, RegisterSerializer

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
@api_view(['GET'])
def get_users(request):
    users = customerUser.objects.all()  # ✅ Gọi model mới
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})
    return Response({'error': 'Invalid Credentials'}, status=400)

@api_view(['GET'])
def user_profile(request):
    user_id = request.data.get('user_id')
    try:
        user = customerUser.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except customerUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


def user_list(request):
    return render(request, 'customer/templates/user_list.html')
