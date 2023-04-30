# from rest_framework import serializers
# from rest_auth.serializers import LoginSerializer
# from django.contrib.auth import authenticate 
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class CustomLoginSerializer(LoginSerializer):
#     username = None # supprimez le champ username du modèle d'authentification
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(required = True) 
#     def validate(self, data):
#         # Assurez-vous que l'utilisateur est activé et approuvé
#         user = authenticate(email = data['email'],password = data['password'])
#         if not user.is_active:
#             raise serializers.ValidationError("User account is disabled.")
#         return user

# class LogoutView(APIView):
#     #authentication_classes = (TokenAuthentication,)

#     def post(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user