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
        if (serializer.data['is_dm']):
            if ('dm_session_id' in serializer.data):
                return Response({'detail': 'Nice try jackass'}, status=status.HTTP_400_BAD_REQUEST)
            dm_serializer = serializers.django_user_serializer(data=serializer.data)
            if (dm_serializer.is_valid()):
                dm_serializer.save()
                return Response(dm_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # new_user = User.objects.create_user(
            #     serializer.data["username"],
            #     serializer.data["email"],
            #     serializer.data["password"]
            # )
            # models.extended_users.objects.create(
            #     is_pc=not serializer.data["is_dm"],
            #     is_dm=serializer.data["is_dm"],
            #     user= new_user
            # )
            # return Response(
            #     serializer.data,
            #     status=status.HTTP_201_CREATED
            # )
        elif ('dm_session_id' in serializer.data):
            if models.dm_session.objects.filter(id=serializer.data['dm_session_id']).first() == None:
                return Response({'detail':'Session ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            # new_user = User.objects.create_user(
            #     serializer.data["username"],
            #     serializer.data["email"],
            #     serializer.data["password"]
            # )
            # models.extended_users.objects.create(
            #     is_pc=not serializer.data["is_dm"],
            #     is_dm=serializer.data["is_dm"],
            #     user= new_user,
            #     dm_session_id=serializer.data['dm_session_id']
            # )
            # return Response(
            #     serializer.data,
            #     status=status.HTTP_201_CREATED
            # )
            extend_serializer = serializers.extended_user_serializer(data=serializer.data)
            if (extend_serializer.is_valid()):
                extend_serializer.save()
                return Response(extend_serializer.data, status=status.HTTP_201_CREATED)
            return Response(extend_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Please enter the session ID given to you by your DM'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


