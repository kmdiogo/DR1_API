from django.shortcuts import render
from rest_framework.decorators import api_view
from DIT import serializers
from django.contrib.auth.models import User
from DIT import models
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def registration_view(request):
    serializer = serializers.user_serializer(data=request.data)
    if (serializer.is_valid()):
        new_user = User.objects.create_user(
            serializer.data["username"],
            serializer.data["email"],
            serializer.data["password"]
        )
        models.extended_users.objects.create(
            is_pc=serializer.data["is_pc"],
            is_dm=serializer.data["is_dm"],
            user= new_user
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
