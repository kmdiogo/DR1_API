from DIT import models
from rest_framework import serializers
from django.contrib.auth.models import User


class characters_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.characters
        fields = '__all__'

class dm_session_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.dm_session
        fields = '__all__'

class creatures_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.creatures
        fields = '__all__'

class user_serializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
    is_dm = serializers.BooleanField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    dm_session_id = serializers.IntegerField (allow_null=True)

class django_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class extended_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

