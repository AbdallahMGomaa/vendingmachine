from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, serializers
from authentication.services import AuthServices


# Create your views here.


class UserRegisterView(generics.GenericAPIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField()
        email = serializers.EmailField()
        password = serializers.CharField()
        role = serializers.CharField()

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        validated_data = input_serializer.validated_data
        user_id, role_id = AuthServices.create_user(**validated_data)
        return JsonResponse({'user_id': user_id, 'role_id': role_id}, status=200)

