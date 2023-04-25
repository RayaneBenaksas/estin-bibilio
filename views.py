from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class BookView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if username is None or password is None or email is None:
        return Response({'error': 'Please provide a valid username, password, and email address'},
                        status=status.HTTP_400_BAD_REQUEST)

    user =  CustomUser.objects.create_user(username=username, password=password, email=email)
    user.save()

    return Response({'success': 'User registered successfully'},
                    status=status.HTTP_201_CREATED)
@api_view(['POST'])
def logout(request):
    logout(request)
    return Response({'success': 'User logged out successfully'})
X
# Create your views here.
