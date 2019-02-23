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
    is_pc = serializers.BooleanField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
