
from django.shortcuts import render
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from rest_framework import status
# from rest_framework.decorators import api_view

# def get(self, request, format=None):
#         books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def register(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     email = request.data.get('email')

#     if username is None or password is None or email is None:
#         return Response({'error': 'Please provide a valid username, password, and email address'},
#                         status=status.HTTP_400_BAD_REQUEST)

#     user =  CustomUser.objects.create_user(username=username, password=password, email=email)
#     user.save()

#     return Response({'success': 'User registered successfully'},
#                     status=status.HTTP_201_CREATED)
# @api_view(['POST'])
# def logout(request):
#     logout(request)
#     return Response({'success': 'User logged out successfully'})
# X //
# # Create your views here. 


# from rest_auth import views
# from rest_framework import permissions
# from rest_auth.views import LoginView

# class EmailLoginView(LoginView):
#     permission_classes = [permissions.AllowAny]

#     def get_response(self):
#         original_response = super().get_response()
#         # Customisez ici la réponse en fonction de vos besoins
#         return original_response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class AuthView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        from django.contrib.auth import login

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
